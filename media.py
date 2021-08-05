import webbrowser


# defiend movie class and defiend movie title,story line,posterand youtube

class movie ():
    def __init__(
        self, movie_title, movie_storyline, poster_images, trailer_youtube
    ):
        self.title = movie_title
        self.storylin = movie_storyline
        self.poster_image_url = poster_images
        self.trailer_youtube_url = trailer_youtube

    # action that open yotube movie
    def show_tralier(self):
        webbrowser.open(self_youtube_url)
