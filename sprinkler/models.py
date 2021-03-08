from sprinkler import db 
from datetime import timedelta

class SprinklerZone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zone_name = db.Column(db.String(80), unique=True, nullable=False)
    pin_number = db.Column(db.Integer, unique=True, nullable=False)
    time_left = db.Column(db.Interval, nullable=True)
    active = db.Column(db.Boolean, nullable=False)

    def __init__(self, zone_name, pin_number, active, time_left=None):
        self.zone_name = zone_name
        self.pin_number = pin_number
        self.active = active
        self.time_left = time_left






