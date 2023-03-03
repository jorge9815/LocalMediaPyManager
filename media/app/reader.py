import os


class Reader:
    def __init__(self):
        # , "Y://Series//Trasmision", "Y://Series//Finalizadas"
        self.LOCAL_DIRECTORIES = ["D://movies", "D://Edited"]
        self.VIDEO_FORMATS = [".mp4", ".avi", ".ts", ".mkv"]

    def read_main_directories(self):
        media_list = []
        for path in self.LOCAL_DIRECTORIES:
            for item in os.listdir(path):
                for supported_format in self.VIDEO_FORMATS:
                    if supported_format in item:
                        media_list.append(item)
        return media_list
