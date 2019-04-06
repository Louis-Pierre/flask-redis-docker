
from flask_restplus import Resource
from flask_restplus import Api
from flask import make_response, session, jsonify


apiStatus = Api(version='1.0', title='API status check',description='Beta version of docker API')
nsCheck = apiStatus.namespace('default', description='Operations related to connection')

@nsCheck.route('/statusCheck')
class APIStatus(Resource):
    def get(self):
        return jsonify({"message":"API up and running !"})


