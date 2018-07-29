from api.restplus import api
from flask_restplus import Resource


ns = api.namespace('sentence', description='NLP on English sentences')


@ns.route('/')
class RumorCollection(Resource):

    # @api.expect(pagination_arguments)
    # @api.marshal_with(sentences)
    def get(self):
        """
        Returns list of blog posts.
        """
        return 'Hello NLP!'
