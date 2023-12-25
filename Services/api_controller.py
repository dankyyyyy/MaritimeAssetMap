from flask import Blueprint, jsonify, request
from tiles_viability_service.bathymetry_helper import BathymetryHelper
from validation.water_depth_validation import WaterDepthValidator
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

api_blueprint = Blueprint('api', __name__)
bathymetry_helper = BathymetryHelper()
water_depth_validator = WaterDepthValidator(bathymetry_helper)

@api_blueprint.route('/water-depth', methods=['GET'])
async def get_water_depth():
    lat = request.args.get('lat', type=float)
    lon = request.args.get('lon', type=float)

    logging.info(f"Received GET lat: {lat}, lot: {lon}")

    result, status_code = await water_depth_validator.validate_and_get_depth(lat, lon)

    logging.info(f"Responding with status: {status_code}, data: {result}")

    return jsonify(result), status_code
