import json

from flask_restplus import Namespace, Resource, fields
from http import HTTPStatus

f = open("static/doc/vehicularData.txt", "r")
namespace = Namespace('Vehiculardata', f.read())
f.closed

location_model = namespace.model('Location', {
    'id': fields.Integer(
        readonly=True,
        description='Location identifier'
    ),
    'name': fields.String(
        required=False,
        description='Location name'
    ),
    'longitude': fields.Float(
        required=False,
        description='Longitude name'
    ),
    'latitude': fields.Float(
        required=False,
        description='Latitude name'
    ),
})

category_model = namespace.model('Category', {
    'id': fields.Integer(
        readonly=False,
        description='Category identifier'
    ),
    'name': fields.String(
        required=False,
        description='Category name'
    )
})

tag_model = namespace.model('Tag', {
    'id': fields.Integer(
        readonly=True,
        description='Tag identifier'
    ),
    'name': fields.String(
        required=False,
        description='Tag name'
    )
})

vehiculardata_model = namespace.model('VehicularData', {
    'id': fields.Integer(
        readonly=True,
        description='VehicularData identifier'
    ),
    'category': fields.Nested(
        category_model,
        description='category',
        as_list=False,
        example ={'name': 'category name'}
    ),
    'name': fields.String(
        required=True,
        description='VehicularData name',
        example = 'my name'
    ),
    'photoUrls': fields.List(
        fields.String,
        required=True,
        description='Url name',
        example=['https://www.challenges.fr/assets/img/2018/08/27/cover-r4x3w1000-5b84072224873-pbc18-conference-09-jpg.jpg']
    ),
    'location': fields.Nested(
        location_model,
        description='location',
        as_list=False,
        required=False,
        example={'name': 'berlin','longitude': 125.258777,'latitude': 785455.25545}
    ),
    'tag': fields.Nested(
        tag_model,
        description='Tag',
        as_list=True,
        required=False,
        example=[{"name": "tag 4"},{"name": "tag 5"}]
    )
})

f = open('static/veihicular_example.txt')
vehiculardata_example = json.load(f)
f.close()

@namespace.route('')
class vehiculardata(Resource):

    @namespace.response(400, 'vehiculardata with the given name already exists')
    @namespace.response(405, 'Invalid input')
    @namespace.response(500, 'Internal Server error')
    @namespace.expect(vehiculardata_model)
    @namespace.marshal_with(vehiculardata_model, code=HTTPStatus.CREATED)
    def post(self):
        '''Add a new vehicular data'''
        return vehiculardata_example,201