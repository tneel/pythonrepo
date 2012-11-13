from flask import Flask


# configuration
DEBUG = False

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = False
    test = app.config['DEBUG']
    app.run()