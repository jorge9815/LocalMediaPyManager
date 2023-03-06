from json import JSONEncoder

from flask import json


class Video:
    def __init__(self, title, route):
        self.title = title
        self.route = route

    def to_json(self):
        return {
            'title': self.title,
            'route': self.route
        }


class Folder:
    def __init__(self, title, directory, items, videos, image):
        self.title = title
        self.directory = directory
        self.items_amount = items
        self.videos = videos
        self.image = image

    def to_json(self):
        return {
            'title': self.title,
            'directory': self.directory,
            'items_amount': self.items_amount,
            'self.videos': self.videos,
            'self.image': self.image
        }
