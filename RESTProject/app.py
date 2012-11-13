# http://publish.luisrei.com/articles/flaskrest.html


from flask import Flask, url_for, request, json, jsonify
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

# ----------Args (Hello)--------------------------------
@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'
    
    
@app.route('/helloJSON', methods = ['GET'])
def api_helloJSON():
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    # jsonify is an utility that replaces
    # js = json.dumps(data)
    # resp = Response(js, status=200, mimetype='application/json')
    resp = jsonify(data)
    resp.status_code = 200
    
    resp.headers['Link'] = 'http://www.paypal.com'
    return resp

# ----------Echo-----------------------------------
@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PATCH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"

# ----------Using request headers-----------------------------------

@app.route('/messages', methods = ['POST'])
def api_message():

    if request.headers['Content-Type'].startswith('text/plain'):
        return "Text Message: " + request.data
    elif request.headers['Content-Type'].startswith('application/json'):
        return "JSON Message: " + json.dumps(request.json)
    elif request.headers['Content-Type'].startswith('application/octet-stream'):
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"
    else:
        return "415 Unsupported Media Type ;)"

# ----------With error handler-----------------------------------
@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

@app.route('/users/<userid>', methods = ['GET'])
def api_users(userid):
    users = {'1':'john', '2':'steve', '3':'bill'}    
    if userid in users:
        return jsonify({'userid' : users[userid]})
    else:
        return not_found()
    
# ----------Main-----------------------------------
if __name__ == '__main__':
    app.debug = False
    app.run()