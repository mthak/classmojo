import logging
import traceback

from flask import Flask
from battle.config.config import Config

from api import blueprint as api

app = Flask(__name__)
app.register_blueprint(api)

log = logging.getLogger(__name__)

'''@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not Config.FLASK_DEBUG:
        return {'message': message}, 500

'''
if __name__ == '__main__':
    app.run(debug=True)