import logging

from flask import abort, request, g, Response, make_response, jsonify, current_app
from flask_restplus import Namespace, Resource, fields, marshal_with
from battle.db.connect import post_meta
from battle.db.models import Battle
log = logging.getLogger(__name__)

posts_api = Namespace('postmeta', description='post information about bigbang')
model = posts_api.model('Model', {
    'name': fields.String,
    'address': fields.String,
    'date_updated': fields.DateTime(dt_format='rfc822'),
})

#ns = api.namespace('post', description='Operations related to data post')



@posts_api.route('')
@posts_api.response("200", "updated successfully")
class posts(Resource):

    @posts_api.expect(model)
    def post(self):
        """
        Update metadata of bigbang.
        """
        data = request.get_json()
        post_meta(data)
        return None, 204