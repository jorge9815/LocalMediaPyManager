import os

from media.domain.entity.media import Video, Folder


class Reader:

    def __init__(self):
        # , "Y://Series//Trasmision", "Y://Series//Finalizadas"
        self.LOCAL_DIRECTORIES = ["D://movies", "D://Edited"]
        self.VIDEO_FORMATS = [".mp4", ".avi", ".ts", ".mkv", ".srt"]
        self.media_collection = []

    def read_main_directories(self):
        self.media_collection = []
        for path in self.LOCAL_DIRECTORIES:
            for item in os.listdir(path):
                self.obtain_files(item, path)
        return self.media_collection

    def obtain_files(self, item, path):
        for supported_format in self.VIDEO_FORMATS:
            if supported_format in item:
                self.add_video(item, path)
                break
        else:
            new_path = f"{path}//{item}"
            subdirectories = os.listdir(new_path)

            video_list = []
            for item_in_folder in subdirectories:
                for supported_format2 in self.VIDEO_FORMATS:
                    if supported_format2 in item_in_folder:
                        video_list.append(Video(item_in_folder, path))
                        break
            folder = Folder(item, path, len(subdirectories), video_list, [])
            self.media_collection.append(folder.toJSON())

    def add_video(self, item, path):
        vid = Video(item, path)
        self.media_collection.append(vid.toJSON())

    def get_files_with_suported_format(self, item, path):
        for supported_format in self.VIDEO_FORMATS:
            if supported_format in item:
                self.add_video(item, path)
