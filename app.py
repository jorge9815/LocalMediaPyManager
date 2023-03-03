from flask import Flask


from media.app.reader import Reader

app = Flask(__name__)
readerO = Reader()


@app.route('/')
def hello_world():  # put application's code here
    print(readerO.read_main_directories())
    return '<p>Hello World!</p>'


if __name__ == '__main__':
    app.run()
