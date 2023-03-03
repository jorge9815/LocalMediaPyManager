from flask import Flask

from media.app.reader import Reader

app = Flask(__name__)
readerO = Reader()


@app.route('/media', methods=['GET'])
def get_media():
    return readerO.read_main_directories()


@app.route("/media/<video_title>")
def get_video_stream(video_title):
    print(video_title)
    return readerO.get_video_info(video_title)


if __name__ == '__main__':
    app.run()
