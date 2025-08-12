from engine import route

@route('/hello', method='GET')
def hello():
    return "<h1>Hello, World!<h2>"

hello()