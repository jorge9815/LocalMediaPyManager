from json import JSONEncoder

from flask import json


class Video:
    def __init__(self, title, route):
        self.title = title
        self.route = route

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class Folder:
    def __init__(self, title, directory, items, videos, image):
        self.title = title
        self.directory = directory
        self.items_amount = items
        self.videos = videos
        self.image = image

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)
