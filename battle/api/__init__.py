from flask import Blueprint
from flask_restplus import Api

from .post import posts_api

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(
    blueprint, title='BigBattle API',
    version='1.0', description='description',
)

api.add_namespace(posts_api, path='/postmeta')
