from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import json


basedir = os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '/data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

Response.default_mimetype='application/JSON'

from sprinkler.models import SprinklerZone, Schedule
db.create_all()

@app.route('/zone/<int:zone_id>', methods=['GET', 'PUT'])
@app.route('/zone/', methods=['POST', 'GET'])
def zone(zone_id=None):
    
    if request.method == 'GET':
        if zone_id == None:
            return Response(__model_to_dict__(SprinklerZone.query.all()), status=200, mimetype='application/JSON' )
        
        zone = SprinklerZone.query.filter_by(id=zone_id).first()
        if zone == None:
            return Response(status=404)
        result = zone.__dict__
        del result['_sa_instance_state']
        return Response(json.dumps(result), status=404)

    if request.method == 'POST':
        new_zone = SprinklerZone(request.form['zone_name'], request.form['pin_number'], False)
        db.session.add(new_zone)
        db.session.commit()
        return Response(status=201)


    if request.method == 'PUT':
        zone = SprinklerZone.query.filter_by(id=zone_id).first()

        if zone == None:
            return Response(status=404)

        if "zone_name" in request.form:
            zone.zone_name = request.form['zone_name']

        if "pin_number" in request.form:
            zone.pin_number = request.form['pin_number']
        


        db.session.add(zone)
        db.session.commit()
        return Response(status=200)

        


@app.route('/schedule/', methods=['GET', 'POST'])
@app.route('/schedule/<int:schedule_id>', methods=['GET', 'PUT'])
def schedule(schedule_id=None):

    if request.method == 'GET' 
        if schedule_id == None:
            return Response(__model_to_dict__(Schedule.query.all()), status=200, mimetype='application/JSON' )

        schedule = Schedule.query.filter_by(id=schedule_id).first()
        if schedule == None:
            return Response(status=404)
        result = schedule.__dict__
        del result['_sa_instance_state']
        return Response(json.dumps(result), status=404)

    if request.method == 'POST':
        new_schedule = Schedule(request.form['schedule_name'], request.form['biweekly'], request.form['days_of_week'], request.form['pin_numbers'])

        #TODO: Add scheduler code for new schedule

        db.session.add(new_schedule)
        db.session.commit()
        return Response(status=201)

    if request.method == 'PUT':
        schedule = Schedule.query.filter_by(id=schedule_id).first()

        if schedule == None:
            return Response(status=404)

        if "schedule_name" in request.form:
            schedule.schedule_name = request.form['schedule_name']

        if biweekly in request.form:
            schedule.biweekly = request.form['biweekly']

        if days_of_week in request.form:
            schedule.days_of_week = request.form['days_of_week']

        if pin_numbers in request.form:
            schedule.pin_numbers = request.form['days_of_week']


        if biweekly in request.form || days_of_week in request.form:
            pass
            #TODO: Add code to adjust scheduler 
            


def __model_to_dict__(model_obj):
    #Creates a dictionary object representing a list of SQLAlchemy model objects
    dict_list = []
    

    for obj in model_obj:
        dict_obj = {}
        for attr in obj.__dict__:
            
            #Ignore _sa_instance_state 
            if attr == '_sa_instance_state':
                continue

            dict_obj[attr] = obj.__dict__[attr]
        
        dict_list.append(dict_obj)

    return json.dumps(dict_list)
