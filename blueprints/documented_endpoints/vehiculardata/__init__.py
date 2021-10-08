from flask import request
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
        readonly=True,
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
        as_list=False
    ),
    'name': fields.String(
        required=True,
        description='VehicularData name',
        example = 'cdu'
    ),
    'photoUrls': fields.Url(
        url = fields.Url('test'),
        required=True
    ),
    'location': fields.Nested(
        location_model,
        description='location',
        as_list=False,
        required=False
    ),
    'tag': fields.Nested(
        tag_model,
        description='Tag',
        as_list=True,
        required=False
    )
})


vehiculardata_example = {'id': 1, 'name': 'Delorean'}

@namespace.doc(description='Describing GET method', tags=['zzzz qsqsq', 'ici'])
@namespace.route('')
class vehiculardata(Resource):

    @namespace.response(400, 'vehiculardata with the given name already exists')
    @namespace.response(405, 'Invalid input')
    @namespace.response(500, 'Internal Server error')
    @namespace.expect(vehiculardata_model)
    @namespace.marshal_with(vehiculardata_model, code=HTTPStatus.CREATED)
    def post(self):
        '''Add a new vehicular data'''
        if request.json['name'] == 'Entity name':
            namespace.abort(400, 'Entity with the given name already exists')

        return vehiculardata_example, 201


