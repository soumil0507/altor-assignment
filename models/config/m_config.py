from config import db

class Config(db.Model):

    __tablename__ = 'm_config'

    id = db.Column(db.Integer)
    username = db.Column(db.String(50), nullable=False, primary_key=True)
    device_brand = db.Column(db.String(50))
    model = db.Column(db.String(50))
    sdk_int = db.Column(db.Integer)
    processor = db.Column(db.String(50))
    vehicle_type = db.Column(db.String(50))
    vehicle_brand = db.Column(db.String(50))
    vehicle_cc = db.Column(db.String(50))
    zone = db.Column(db.String(50))

    def toJSON(self):
        pass

