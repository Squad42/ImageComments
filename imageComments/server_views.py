import json
from flask import request, render_template, jsonify, session, g
from imageComments.server import app
from imageComments.models import ImageComments
from imageComments.manage_db import get_all, add_instance, delete_instance, edit_instance
from functools import wraps
import jwt
import datetime


def jwt_token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):

        if "jwt_token" not in session:
            return jsonify({"message": "Auth token is missing!"}), 403

        token = session["jwt_token"]

        if not token:
            return jsonify({"message": "Unknown token type!"}), 403

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
            g.user_info = data
            app.logger.info("Logged in user: %s", g.user_info["username"])
        except:
            return jsonify({"message": "Token is invalid!"}), 403

        return func(*args, **kwargs)

    return decorated


@app.route("/", methods=["GET"])
def index():
    return jsonify({"Hello": "world"})


@app.route("/comments", methods=["GET"])
def fetch():

    if not app.config["DB_ONLINE"]:
        print("ERROR: Database connection is down!")
        response = jsonify(service_status="Bad gateway: check DB connection!", service_code=502)
        return response, 200

    image_comments = get_all(ImageComments)
    all_image_comments = []
    for img_comment in image_comments:
        new_image_comment = {
            "username": img_comment.username,
            "text": img_comment.text,
            "img_uri": img_comment.img_uri,
            "created-on": img_comment.created_datetime.strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        all_image_comments.append(new_image_comment)
    return json.dumps(all_image_comments), 200


@app.route("/comments/filter/<path:img_url>", methods=["GET"])
def fetch_filtered(img_url):

    if not app.config["DB_ONLINE"]:
        print("ERROR: Database connection is down!")
        response = jsonify(service_status="Bad gateway: check DB connection!", service_code=502)
        return response, 200

    # print("FILTER_IMG: " + img_url, flush=True)
    # img_url = str(img_url)
    # image_comments = ImageComments.query.filter_by(img_uri=img_url).all()
    # print(image_comments, flush=True)
    # all_image_comments = []
    # for img_comment in image_comments:
    #     new_image_comment = {
    #         "username": img_comment.username,
    #         "text": img_comment.text,
    #         "img_uri": img_comment.img_uri,
    #         "created-on": img_comment.created_datetime.strftime("%Y-%m-%dT%H:%M:%SZ"),
    #     }
    #     all_image_comments.append(new_image_comment)
    # return json.dumps(all_image_comments), 200
    # all_image_comments = []
    image_comments = get_all(ImageComments)
    all_image_comments = {}
    for img_comment in image_comments:
        # print("COMPARING:    ", flush=True)
        # print(img_comment.img_uri + "   vs   " + img_url + "\n", flush=True)
        if (
            img_comment.img_uri.replace("?dl=1", "").replace("?dl=0", "").replace("?raw=1", "")
            == img_url
        ):
            # new_image_comment = {"username": img_comment.username, "text": img_comment.text}
            all_image_comments[img_comment.username] = img_comment.text
    return json.dumps(all_image_comments), 200


@app.route("/comments/add", methods=["POST"])
def add():

    if not app.config["DB_ONLINE"]:
        print("ERROR: Database connection is down!")
        response = jsonify(service_status="Bad gateway: check DB connection!", service_code=502)
        return response, 200

    data = request.get_json()
    username = data["username"]
    text = data["text"]
    img_uri = data["img_uri"]
    created_datetime = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

    add_instance(
        ImageComments,
        username=username,
        text=text,
        img_uri=img_uri,
        created_datetime=created_datetime,
    )
    return json.dumps("Added"), 200
