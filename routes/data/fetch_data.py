from flask import Blueprint, jsonify, request, render_template
from models.config.m_config import Config
import requests
import json
import pandas as pd
from config import ASSIGNMENT_DATA_URI


from config import db

fetch_data_bp = Blueprint("fetch_data_bp", __name__)

@fetch_data_bp.route("/")
def fetch_all_data():
    try:
        response = requests.get(ASSIGNMENT_DATA_URI)
        json_data = response.json()['data']
        main_df = pd.DataFrame(json_data)
        print(main_df.head())
        for _, row in main_df.iterrows():
            
            data = Config(username=row['username'],
                          device_brand=row['device_brand'],
                          model = row['model'],
                          sdk_int = row['sdk_int'],
                          processor = row['processor'],
                          vehicle_type = row['vehicle_type'],
                          vehicle_brand = row['vehicle_brand'],
                          vehicle_cc = row['vehicle_cc'],
                          zone = row['zone']
                        )

            db.session.add(data)
        
        db.session.commit()

        return jsonify(status = "ok", message = "all data added to database"), 200
    
    except Exception as e:

        print(e)
        return jsonify(status = "error", message = "error in adding data to database"), 400

