import os


class Reader:
    def __init__(self):
        # , "Y://Series//Trasmision", "Y://Series//Finalizadas"
        self.LOCAL_DIRECTORIES = ["D://movies", "D://Edited"]
        self.VIDEO_FORMATS = [".mp4", ".avi", ".ts", ".mkv", ".srt"]
        self.structure = {}

    def read(self):
        for route in self.LOCAL_DIRECTORIES:
            self.get_directory_structure(route)
        return self.structure

    def get_directory_structure(self, path):
        for entry in os.scandir(path):
            if entry.is_dir():
                self.structure[entry.name] = self.get_directory_structure(entry.path)
            else:
            #     for format in self.VIDEO_FORMATS:
            #         if entry.name.endswith(format):
                 self.structure[entry.name] = {
                            'path': entry.path,
                            'type': "video",
                            "size": os.stat(entry).st_size
                        }

    def get_video_info(self, video_title):
        return self.structure[video_title]
