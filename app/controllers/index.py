from flask_restful import Resource
from flask import make_response, render_template


class IndexAPI(Resource):
    def get(self):
        return make_response(render_template('index.html'))


class PiecesIndexAPI(Resource):
    def get(self, nation, month):
        return ''.join(['hi, it is a page for ', nation, ' at ', month])
