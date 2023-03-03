from flask import Flask

from media.app.reader import Reader

app = Flask(__name__)
readerO = Reader()


@app.route('/media', methods=['GET'])
def get_media():
    return readerO.read_main_directories()


if __name__ == '__main__':
    app.run()
