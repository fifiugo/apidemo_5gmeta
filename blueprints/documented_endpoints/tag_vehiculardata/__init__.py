from flask_restplus import Namespace, Resource, fields


f = open("static/doc/VehicleIdentificationData.txt", "r")
namespace_vid = Namespace('VehicleIdentificationData', f.read())
f.closed

f = open("static/doc/VehicleAttributes.txt", "r")
namespace_vehicleattributes = Namespace('VehicleAttributes', f.read())
f.closed

f = open("static/doc/VehicleStatus.txt", "r")
namespace_vehiclestatus = Namespace('VehicleStatus', f.read())
f.closed

f = open("static/doc/VehiclePositionandDynamics.txt", "r")
namespace_vpd = Namespace('VehiclePositionandDynamics', f.read())
f.closed

f = open("static/doc/SensorsVehicleExternalData.txt", "r")
namespace_sve = Namespace('SensorsVehicleExternalData', f.read())
f.closed


@namespace_vid.route('')
class VehicleIdentificationData(Resource):
    pass

@namespace_vehicleattributes.route('')
class VehicleAttributes(Resource):
    pass

@namespace_vehiclestatus.route('')
class VehicleStatus(Resource):
    pass

@namespace_vpd.route('')
class VehiclePositionandDynamics(Resource):
    pass

@namespace_sve.route('')
class SensorsVehicleExternalData(Resource):
    pass