from plivo.app import app

from plivo import routes

app.run(host=app.config['SERVER_NAME'], port=5000)
