import logging

from flask import abort, request, g, Response, make_response, jsonify, current_app
from flask_restplus import Namespace, Resource, fields, marshal_with
from battle.db.dbops import dbops
from battle.db.models import Battle
log = logging.getLogger(__name__)

posts_api = Namespace('postmeta', description='post information about bigbang')
model = posts_api.model('Model', {
   "Developer_Issues" : fields.Integer,
    "Issues_Resolved"  : fields.Integer,
    "Issues_Pending": fields.Integer,
    "Component_Issues": fields.Integer,
    "Component_Failures": fields.List(fields.String),
    "Total_Tickets" : fields.List(fields.String),
    "Jiras" : fields.List(fields.String),
    "Faq_Updated": fields.Integer,
    'date_updated': fields.DateTime()
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
        dbops.post_meta(data)
        return None, 204


    def get(self):
        data = dbops.get_meta()
        return data