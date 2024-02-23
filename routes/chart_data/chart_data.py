from flask import Blueprint, request, jsonify
from models.config.m_config import Config
from config import db
from sqlalchemy import or_


# url_prefix = "chart_data"
chart_data_bp = Blueprint('chart_data_bp', __name__)


# PIE CHARTS

# get device_brand distribution
@chart_data_bp.route('/distribution/device_brand', methods=['GET'])
def device_brand_distribution():
    _zone = request.args.getlist('zone')
    try:
        if _zone:
            counts = db.session.query(Config.zone, Config.device_brand,  db.func.count()) \
                            .filter(or_(*[Config.zone == zone for zone in _zone])) \
                            .group_by(Config.device_brand) \
                            .group_by(Config.zone) \
                            .all()
            # print(counts)
            
            if counts:
                result = [ {"zone":zone, "device_brand": device_brand, "count": count} for zone, device_brand, count in counts]
                return jsonify(status = "ok", message = f"fetched {_zone} wise device_brand distribution", data = result), 200
            else:
                return jsonify(status = "ok", message = "Zone not found"), 200
        else:
            counts = db.session.query(Config.device_brand, db.func.count()) \
                            .group_by(Config.device_brand) \
                            .all()
            
            result = [{"device_brand": device_brand, "count": count} for device_brand, count in counts]
            return jsonify(status = "ok", message = "fetched all zone vehicle cc distribution", data = result), 200

    except Exception as e:
        print(e)
        return jsonify(status = "error", message = "error in fetching data"), 400

# get vehicle_brand distribution
@chart_data_bp.route('/distribution/vehicle_brand', methods=['GET'])
def vehicle_brand_distribution():
    _zone = request.args.getlist('zone')
    try:
        if _zone:
            counts = db.session.query(Config.zone, Config.vehicle_brand,  db.func.count()) \
                            .filter(or_(*[Config.zone == zone for zone in _zone])) \
                            .group_by(Config.vehicle_brand) \
                            .group_by(Config.zone) \
                            .all()
            # print(counts)
            
            if counts:
                result = [ {"zone":zone, "vehicle_brand": vehicle_brand, "count": count} for zone, vehicle_brand, count in counts]
                return jsonify(status = "ok", message = f"fetched {_zone} wise vehicle_brand distribution", data = result), 200
            else:
                return jsonify(status = "ok", message = "Zone not found"), 200
        else:
            counts = db.session.query(Config.vehicle_brand, db.func.count()) \
                            .group_by(Config.vehicle_brand) \
                            .all()
            
            result = [{"vehicle_brand": vehicle_brand, "count": count} for vehicle_brand, count in counts]
            return jsonify(status = "ok", message = "fetched all zone vehicle cc distribution", data = result), 200

    except Exception as e:
        print(e)
        return jsonify(status = "error", message = "error in fetching data"), 400


# get vehicle_cc distribution for multiple zones
@chart_data_bp.route('/distribution/vehicle_cc', methods=['GET'])
def vehicle_cc_distribution():
    _zone = request.args.getlist('zone')
    try:
        if _zone:
            counts = db.session.query(Config.zone, Config.vehicle_cc,  db.func.count()) \
                            .filter(or_(*[Config.zone == zone for zone in _zone])) \
                            .group_by(Config.vehicle_cc) \
                            .group_by(Config.zone) \
                            .all()
            # print(counts)
            
            if counts:
                result = [ {"zone":zone, "vehicle_cc": vehicle_cc, "count": count} for zone, vehicle_cc, count in counts]
                return jsonify(status = "ok", message = f"fetched {_zone} wise vehicle cc distribution", data = result), 200
            else:
                return jsonify(status = "ok", message = "Zone not found"), 200
        else:
            counts = db.session.query(Config.vehicle_cc, db.func.count()) \
                            .group_by(Config.vehicle_cc) \
                            .all()
            
            result = [{"vehicle_cc": vehicle_cc, "count": count} for vehicle_cc, count in counts]
            return jsonify(status = "ok", message = "fetched all zone vehicle cc distribution", data = result), 200

    except Exception as e:
        print(e)
        return jsonify(status = "error", message = "error in fetching data"), 400


# get sdk_int distribution
@chart_data_bp.route('/distribution/sdk_int', methods=['GET'])
def sdk_int_distribution():
    _zone = request.args.getlist('zone')
    try:
        if _zone:
            counts = db.session.query(Config.zone, Config.sdk_int,  db.func.count()) \
                            .filter(or_(*[Config.zone == zone for zone in _zone])) \
                            .group_by(Config.sdk_int) \
                            .group_by(Config.zone) \
                            .all()
            # print(counts)
            
            if counts:
                result = [ {"zone":zone, "sdk_int": sdk_int, "count": count} for zone, sdk_int, count in counts]
                return jsonify(status = "ok", message = f"fetched {_zone} wise sdk_int distribution", data = result), 200
            else:
                return jsonify(status = "ok", message = "Zone not found"), 200
        else:
            counts = db.session.query(Config.sdk_int, db.func.count()) \
                            .group_by(Config.sdk_int) \
                            .all()
            
            result = [{"sdk_int": sdk_int, "count": count} for sdk_int, count in counts]
            return jsonify(status = "ok", message = "fetched all zone sdk_int distribution", data = result), 200

    except Exception as e:
        print(e)
        return jsonify(status = "error", message = "error in fetching data"), 400