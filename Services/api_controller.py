from flask import Blueprint, jsonify, request
from tiles_viability_service.bathymetry_helper import BathymetryHelper
from validation.water_depth_validation import WaterDepthValidator

api_blueprint = Blueprint('api', __name__)
bathymetry_helper = BathymetryHelper()
water_depth_validator = WaterDepthValidator(bathymetry_helper)

@api_blueprint.route('/water-depth', methods=['GET'])
async def get_water_depth():
    lat = request.args.get('lat', type=float)
    lon = request.args.get('lon', type=float)
    
    result, status_code = await water_depth_validator.validate_and_get_depth(lat, lon)
    return jsonify(result), status_code
