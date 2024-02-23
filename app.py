from flask import Flask, render_template
from models.config.m_config import Config
from config import db
from routes.data.fetch_data import fetch_data_bp
from routes.table_data.get_table_data import table_data_bp
from routes.chart_data.chart_data import chart_data_bp
from config import DB_URI, ASSIGNMENT_DATA_URI



def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI


    db.init_app(app)

    app.register_blueprint(fetch_data_bp)
    app.register_blueprint(table_data_bp, url_prefix = "/table_data")
    app.register_blueprint(chart_data_bp, url_prefix = "/chart_data")
    with app.app_context():
        
        db.create_all()
        db.session.commit()

        return app
    

    
if __name__ == '__main__':

    app = create_app()

    app.run(debug=True)