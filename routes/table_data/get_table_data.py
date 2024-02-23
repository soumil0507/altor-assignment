from flask import Blueprint, jsonify, request
from models.config.m_config import Config

table_data_bp = Blueprint("table_data_bp", __name__)

# url_prefix = "table_data"

# get all table data
@table_data_bp.route("/get_all", methods=["GET"])
def get_all_table_data():
    try:
        
        data = Config.query.all()
        table_data_list = []
        # name, zone, device_brand, sdk_int, vehicle_brand, vehicle_cc
        for conf_data in data:

            table_data = {"name":conf_data.username, "device_brand":conf_data.device_brand, "sdk_int":conf_data.sdk_int, "vehicle_brand": conf_data.vehicle_brand, "vehicle_cc": conf_data.vehicle_cc, "zone": conf_data.zone}

            table_data_list.append(table_data)
        
        return jsonify(status = "success", message = "fetched all table data", data = table_data_list), 200
    except Exception as e:
        print(e)
        return jsonify(status = "error", message = "error in fetching table data"), 500
    
# get table data by username
@table_data_bp.route("/get_user_data/<username>", methods = ["GET"])
def get_user_data(username):

    try:
        conf_data = Config.query.filter_by(username = username).first()
        # print(conf_data.username)
        table_data_list = []
        # name, zone, device_brand, sdk_int, vehicle_brand, vehicle_cc

        table_data = {"name":conf_data.username, "device_brand":conf_data.device_brand, "sdk_int":conf_data.sdk_int, "vehicle_brand": conf_data.vehicle_brand, "vehicle_cc": conf_data.vehicle_cc, "zone": conf_data.zone}

        table_data_list.append(table_data)
        
        return jsonify(status = "success", message = "fetched user data", data = table_data_list), 200
    except Exception as e:
        print(e)
        return jsonify(status = "error", message = "error in fetching table user data"), 500
    

# get table data by zone, device_brand, vehicle_brand, vehicle_cc, sdk_int
# applying dynamic filter
@table_data_bp.route("/get_filter_data", methods = ["GET", "POST"])
def get_zone_data():

    filter = request.json

    try:
        # data = Config.query.filter_by(zone = zone).all()

        query = Config.query
        for filter_key, filter_value in filter.items():
            print(getattr(Config, filter_key))
            # quey = query.filter_by(**{filter_key: filter_value})
            query = query.filter(getattr(Config, filter_key) == filter_value)
        
        data = query.all() 
        
        table_data_list = []
        # name, zone, device_brand, sdk_int, vehicle_brand, vehicle_cc
        for conf_data in data:

            table_data = {"name":conf_data.username, "device_brand":conf_data.device_brand, "sdk_int":conf_data.sdk_int, "vehicle_brand": conf_data.vehicle_brand, "vehicle_cc": conf_data.vehicle_cc, "zone": conf_data.zone}

            table_data_list.append(table_data)

        return jsonify(status = "success", message = "fetched zone table data", data = table_data_list), 200
    
    except Exception as e:
        
        print(e)
        
        return jsonify(status = "error", message = "error in fetching zone data"), 400
    
