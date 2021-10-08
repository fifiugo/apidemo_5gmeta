from flask import Blueprint
from flask_restplus import Api
from blueprints.documented_endpoints.tag_vehiculardata import namespace_vid as vid_ns
from blueprints.documented_endpoints.tag_vehiculardata import namespace_vehicleattributes as vehicleattribute_ns
from blueprints.documented_endpoints.tag_vehiculardata import namespace_vehiclestatus as vehiclestatus_ns
from blueprints.documented_endpoints.tag_vehiculardata import namespace_vpd as vpd_ns
from blueprints.documented_endpoints.tag_vehiculardata import namespace_sve as sve_ns
from blueprints.documented_endpoints.vehiculardata import namespace as vehicular_ns

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API'
    },
    'oauth2': {
        'type': 'oauth2',
        'flow': 'accessCode',
        'tokenUrl': 'https://somewhere.com/token',
        'authorizationUrl': 'https://somewhere.com/auth',
        'scopes': {
            'read': 'Grant read-only access',
            'write': 'Grant read-write access',
        }
    }
}


blueprint = Blueprint('documented_api', __name__, url_prefix='/api')

api_extension = Api(
    blueprint,
    title='Flask RESTplus 5GMeta Demo',
    version='1.0',
    description='Application demo to demonstrate 5GMETA vehicule Data API',
    doc='/doc',
    authorizations=authorizations
)


api_extension.add_namespace(vehicular_ns)
api_extension.add_namespace(vid_ns)
api_extension.add_namespace(vehicleattribute_ns)
api_extension.add_namespace(vehiclestatus_ns)
api_extension.add_namespace(vpd_ns)
api_extension.add_namespace(sve_ns)