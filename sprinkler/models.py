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

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    schedule_name = db.Column(db.String(80), unique=True, nullable=False)
    biweekly = db.Column(db.Boolean(), nullable=False)
    days_of_week = db.Column(db.String, nullable=False)
    pin_numbers = db.Column(db.String, nullable=False)

    def __init__(self, schedule_name, biweekly, days_of_week, pin_numbers):
        self.schedule_name = schedule_name
        self.biweekly = biweekly
        self.days_of_week = days_of_week
        self.pin_numbers = pin_numbers

    

    
    








