from flask import Flask, request
app = Flask(__name__)

@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'
    

# ----------Main-----------------------------------
if __name__ == '__main__':
    app.debug = False
    app.run()    