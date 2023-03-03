class Video:
    def __int__(self, title, route):
        self.title = title
        self.route = route


class Folder:
    def __init__(self, title, directory, items, videos, image):
        self.title = title
        self.directory = directory
        self.items_amount = items
        self.videos = videos
        self.image = image
