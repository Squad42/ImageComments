from imageComments.models import ImageComments


def db_load_example_data(app, db):

    image_comments = [
        ImageComments(
            "admin1",
            "I love this picture!!",
            "https://www.dropbox.com/s/uwlodj52lmc0oxi/c3c.png?dl=1",
            "2019-11-22T16:14:03Z",
        ),
        ImageComments(
            "admin1",
            "My new wallpaper, for sure :D",
            "https://rso-imageportal.s3.eu-central-1.amazonaws.com/Screenshot_from_2019-11-11_02-10-07.png",
            "2019-11-22T16:15:13Z",
        ),
        ImageComments(
            "admin2",
            "Love the photo!",
            "https://www.dropbox.com/s/9fccuidhjbbqdaq/173533.jpg?dl=1",
            "2019-11-22T16:14:03Z",
        ),
        ImageComments(
            "user4",
            "Love the photo!",
            "https://www.dropbox.com/s/fs2tdth9187a6tr/deer-artwork.jpg?dl=1",
            "2019-11-22T16:14:03Z",
        ),
        ImageComments(
            "user6",
            "My new wallpaper, for sure :D",
            "https://rso-imageportal.s3.eu-central-1.amazonaws.com/adrianfelipepera_traslasierra.jpg",
            "2019-11-22T16:15:13Z",
        ),
        ImageComments(
            "user6",
            "Love the photo!",
            "https://www.dropbox.com/s/x0m8xm91wuvps0z/gdmlock.jpg?dl=1",
            "2019-11-22T16:14:03Z",
        ),
        ImageComments(
            "admin2",
            "Love the photo!",
            "https://www.dropbox.com/s/fqpguogsr8mdct2/roa050118fea-corvette-08-1522693637.jpg?dl=1",
            "2019-11-22T16:14:03Z",
        ),
        ImageComments(
            "user3",
            "My new wallpaper, for sure :D",
            "https://rso-imageportal.s3.eu-central-1.amazonaws.com/wireframed-deer.jpg",
            "2019-11-22T16:15:13Z",
        ),
        ImageComments(
            "user3",
            "Love the photo!",
            "https://www.dropbox.com/s/u90wot3rttdcbbo/wp1828915-programmer-wallpapers.png?dl=1",
            "2019-11-22T16:14:03Z",
        ),
        ImageComments(
            "admin1",
            "My new wallpaper, for sure :D",
            "https://rso-imageportal.s3.eu-central-1.amazonaws.com/test.jpg",
            "2019-11-22T16:15:13Z",
        ),
    ]

    with app.app_context():
        for img_c in image_comments:
            db.session.add(img_c)
        db.session.commit()
