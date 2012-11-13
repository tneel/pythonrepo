
from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)

def check_auth(username, password):
    return username == 'admin' and password == 'secret'

def authenticate():
    message = {'message': "Authenticate."}
    resp = jsonify(message)
    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'
    return resp

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth: 
            return authenticate()
        elif not check_auth(auth.username, auth.password):
            return authenticate("Authentication Failed.")
        return f(*args, **kwargs)
    return decorated

@app.route('/secrets')
@requires_auth
def api_hello():
    return "Shhh this is top secret spy stuff!"

# ----------Main-----------------------------------
if __name__ == '__main__':
    app.debug = False
    app.run()