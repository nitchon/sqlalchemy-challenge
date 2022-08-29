
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt
from datetime import datetime


# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station


# Flask API Coding
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False



#Home Route with Available Routes
@app.route("/")
def home():
    return  (
        "Welcome to the Hawaii Climate App!<br/><br/>"
        f"Available Routes:<br/><br/>"
        f"Precipitation: /api/v1.0/precipitation<br/>"
        f"Stations: /api/v1.0/stations<br/>"
        f"Temperatures for Last Year: /api/v1.0/tobs<br/>"
        f"Temperature Stats from Start Date (yyyy-mm-dd): /api/v1.0/yyyy-mm-dd<br/>"
        f"Temperature Stats from Start Date (yyyy-mm-dd) to End Date (yyyy-mm-dd): /api/v1.0/yyyy-mm-dd/yyyy-mm-dd"
    )

#Precipitation App
@app.route("/api/v1.0/precipitation")
def prcp():
    session = Session(engine)
    precip_query = session.query(Measurement.station,Measurement.date,Measurement.prcp).all()
    session.close()

    prcp_rows = [{"Station":data[0],"Date":data[1],"PRCP":data[2]} for data in precip_query]
    return jsonify(prcp_rows)

#Station App
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    sel = [Station.station,Station.name,Station.latitude,Station.longitude,Station.elevation]
    station_query = session.query(*sel).all()
    session.close()

    station = [{"Station":data[0],"Name":data[1],"Latitude":data[2],"Longitude":data[3],"Elevation":data[4]} for data in station_query]
    return(jsonify(station))

#Temperature App
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    recent = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    recent_date = recent[0]
    year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
    most_active = session.query(Measurement.station,func.count(Measurement.station)).\
        group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
    most_active_station = most_active[0][0]
    temp_data=session.query(Measurement.station,Measurement.date,Measurement.tobs).filter(Measurement.date <= recent_date).\
        filter(Measurement.date >= year_ago).\
        filter(Measurement.station==most_active_station).all()
    session.close()
    temp_rows = [{"Station":data[0],"Date":data[1],"TOBS":data[2]} for data in temp_data]
    return(jsonify(temp_rows))

#Temperature Stats with Start Date query
@app.route("/api/v1.0/<start>")
def open_temp_stats(start):
    session = Session(engine)
    open_temp_stats = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    session.close()
    temp = [{"Minimum Temperature":data[0],"Maximum Temperature":data[1],"Average Temperature":data[1]} for data in open_temp_stats]
    return(jsonify(temp))

#Temperature Stats with Start Date/End Date query
@app.route("/api/v1.0/<start>/<end>")
def closed_temp_stats(start,end):
    session = Session(engine)
    closed_temp_stats = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date<=end).all()
    session.close()
    temp = [{"Minimum Temperature":data[0],"Maximum Temperature":data[1],"Average Temperature":data[1]} for data in closed_temp_stats]
    return(jsonify(temp))



if __name__ == "__main__":
    app.run(debug=True)