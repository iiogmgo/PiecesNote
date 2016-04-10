from flask.ext.restful import Api
from app.controllers.index import IndexAPI, PiecesIndexAPI


def create_restful_app(app):
    api = Api(app)
    api.add_resource(IndexAPI, '/', endpoint='index')
    api.add_resource(PiecesIndexAPI, '/<string:nation>/<string:month>', endpoint='pieces_index')

    return api
