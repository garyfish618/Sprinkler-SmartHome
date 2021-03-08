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

from sprinkler.models import SprinklerZone
db.create_all()

@app.route('/zones/', methods=['GET'])
@app.route('/zone/<int:zone_id>', methods=['GET'])
@app.route('/zone/', methods=['POST'])
def zone(zone_id=None):
    
    if request.method == 'GET':
        if zone_id == None:
            return Response(json.dumps(__model_to_dict__(SprinklerZone.query.all())), status=200, mimetype='application/JSON' )
        
        zone = SprinklerZone.query.filter_by(id=zone_id).first()

        if zone == None:
            return Response(status=404)

        return Response(zone, status=404)

    if request.method == 'POST':
        print("ZONE" + request.form['zone_name'])
        new_zone = SprinklerZone(request.form['zone_name'], request.form['pin_number'], False)
        db.session.add(new_zone)
        db.session.commit()
        return Response(status=201)





def __model_to_dict__(model_obj):
    #Creates a dictionary object representing a list of SQLAlchemy model objects
    dict_obj = {}

    for obj in model_obj:
        for attr in obj.__dict__:
            #Ignore _sa_instance_state 
            if attr == '_sa_instance_state':
                continue

            dict_obj[attr] = obj.__dict__[attr]

    return dict_obj


