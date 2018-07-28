import os

from plivo.app import app

from plivo import routes

if app.config['DEBUG'] == False:
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
elif app.config['DEBUG'] == True:
    app.run(host='127.0.0.1', port=5000)
