from flask.ext.restful import Api
from app.controllers.index import IndexAPI


def create_restful_app(app):
    api = Api(app)
    api.add_resource(IndexAPI, '/', endpoint='index')

    return api
