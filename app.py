from flask import Flask, jsonify

from media.app.reader import Reader

app = Flask(__name__)

readerO = Reader()


@app.route('/media', methods=['GET'])
def get_media():
    return jsonify(readerO.read_main_directories())


@app.route("/media/<video_title>", methods=['GET'])
def get_video_stream(video_title):
    print(video_title)
    return jsonify(readerO.get_video_info(video_title))


if __name__ == '__main__':
    app.run()
