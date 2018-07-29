from restplus import api
from flask_restplus import fields

sentence = api.model('sentence', {
    'id': fields.Integer(readOnly=True, description='unique identifier of a sentence'),
    'content': fields.String(required=True, description='sentence content'),
    'pub_date': fields.DateTime
})
