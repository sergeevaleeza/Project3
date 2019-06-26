import os
import pandas as pd
import geojson
import json
from flask import request
from flask import send_file

from flask import (
    Flask,
    render_template,
    jsonify)
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
from flask_sqlalchemy import SQLAlchemy
# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data/cancer.sqlite"

db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
cancer_data = Base.classes.incidence
risk_data = Base.classes.risk
state_data = Base.classes.census
death_data = Base.classes.mortality


class Cancer(db.Model):


    __tablename__ = 'incidence'
    State_code = db.Column(db.String(255))
    State = db.Column(db.String(255), primary_key=True)
    FIPS = db.Column(db.Integer)
    bladder_count = db.Column(db.Integer)
    bladder_rate = db.Column(db.Numeric)
    brain_count = db.Column(db.Integer)
    brain_rate = db.Column(db.Numeric)
    breast_count = db.Column(db.Integer)
    breast_rate = db.Column(db.Numeric)
    breast_insitu_count = db.Column(db.Integer)
    breast_insitu_rate = db.Column(db.Numeric)
    cervix_count = db.Column(db.Integer)
    cervix_rate = db.Column(db.Numeric)
    child_less_15_count = db.Column(db.Integer)
    child_less_15_rate = db.Column(db.Numeric)
    child_less_20_count = db.Column(db.Integer)
    child_less_20_rate = db.Column(db.Numeric)
    db.Colon_rectum_count = db.Column(db.Integer)
    db.Colon_rectum_rate = db.Column(db.Numeric)
    esophagus_count = db.Column(db.Integer)
    esophagus_rate = db.Column(db.Numeric)
    kidney_count = db.Column(db.Integer)
    kidney_rate = db.Column(db.Numeric)
    leukemia_count = db.Column(db.Integer)
    leukemia_rate = db.Column(db.Numeric)
    liver_count = db.Column(db.Integer)
    liver_rate = db.Column(db.Numeric)
    lung_count = db.Column(db.Integer)
    lung_rate = db.Column(db.Numeric)
    melanoma_count = db.Column(db.Integer)
    melanoma_rate = db.Column(db.Numeric)
    non_HodgkinL_count = db.Column(db.Integer)
    non_HodgkinL_rate = db.Column(db.Numeric)
    oral_pharynx_count = db.Column(db.Integer)
    oral_pharynx_rate = db.Column(db.Numeric)
    ovary_count = db.Column(db.Integer)
    ovary_rate = db.Column(db.Numeric)
    pancreas_count = db.Column(db.Integer)
    pancreas_rate = db.Column(db.Numeric)
    prostate_count = db.Column(db.Integer)
    prostate_rate = db.Column(db.Numeric)
    stomach_count = db.Column(db.Integer)
    stomach_rate = db.Column(db.Numeric)
    thyroid_count = db.Column(db.Integer)
    thyroid_rate = db.Column(db.Numeric)
    uterus_count = db.Column(db.Integer)
    uterus_rate = db.Column(db.Numeric)
    breast_insitu_count = db.Column(db.Integer)
    breast_insitu_rate = db.Column(db.Numeric)
    child_less_20_count = db.Column(db.Integer)
    child_less_20_rate = db.Column(db.Numeric)


    __tablename__ = 'mortality'
    State_code = db.Column(db.String(255))
    State = db.Column(db.String(255), primary_key=True)
    FIPS = db.Column(db.Integer)
    bladder_count = db.Column(db.Integer)
    bladder_rate = db.Column(db.Numeric)
    brain_count = db.Column(db.Integer)
    brain_rate = db.Column(db.Numeric)
    breast_count = db.Column(db.Integer)
    breast_rate = db.Column(db.Numeric)
    breast_insitu_count = db.Column(db.Integer)
    breast_insitu_rate = db.Column(db.Numeric)
    cervix_count = db.Column(db.Integer)
    cervix_rate = db.Column(db.Numeric)
    child_less_15_count = db.Column(db.Integer)
    child_less_15_rate = db.Column(db.Numeric)
    child_less_20_count = db.Column(db.Integer)
    child_less_20_rate = db.Column(db.Numeric)
    db.Colon_rectum_count = db.Column(db.Integer)
    db.Colon_rectum_rate = db.Column(db.Numeric)
    esophagus_count = db.Column(db.Integer)
    esophagus_rate = db.Column(db.Numeric)
    kidney_count = db.Column(db.Integer)
    kidney_rate = db.Column(db.Numeric)
    leukemia_count = db.Column(db.Integer)
    leukemia_rate = db.Column(db.Numeric)
    liver_count = db.Column(db.Integer)
    liver_rate = db.Column(db.Numeric)
    lung_count = db.Column(db.Integer)
    lung_rate = db.Column(db.Numeric)
    melanoma_count = db.Column(db.Integer)
    melanoma_rate = db.Column(db.Numeric)
    non_HodgkinL_count = db.Column(db.Integer)
    non_HodgkinL_rate = db.Column(db.Numeric)
    oral_pharynx_count = db.Column(db.Integer)
    oral_pharynx_rate = db.Column(db.Numeric)
    ovary_count = db.Column(db.Integer)
    ovary_rate = db.Column(db.Numeric)
    pancreas_count = db.Column(db.Integer)
    pancreas_rate = db.Column(db.Numeric)
    prostate_count = db.Column(db.Integer)
    prostate_rate = db.Column(db.Numeric)
    stomach_count = db.Column(db.Integer)
    stomach_rate = db.Column(db.Numeric)
    thyroid_count = db.Column(db.Integer)
    thyroid_rate = db.Column(db.Numeric)
    uterus_count = db.Column(db.Integer)
    uterus_rate = db.Column(db.Numeric)


    __tablename__ = 'census'
    State_code = db.Column(db.String(255))
    State = db.Column(db.String(255), primary_key=True)
    FIPS = db.Column(db.Integer)
    crowding_count = db.Column(db.Integer)
    crowding_percent = db.Column(db.Numeric)
    education_bachelors_count = db.Column(db.Integer)
    education_bachelors_percent = db.Column(db.Numeric)
    median_family_income_dollars = db.Column(db.Integer)
    uninsured_count = db.Column(db.Integer)
    uninsured_percent = db.Column(db.Numeric)
    below_150_poverty_count = db.Column(db.Integer)
    below_150_poverty_percent = db.Column(db.Numeric)
    unemployed_count = db.Column(db.Integer)
    unemployed_percent = db.Column(db.Numeric)


    __tablename__ = 'risk'
    State_code = db.Column(db.String(255))
    State = db.Column(db.String(255), primary_key=True)
    FIPS = db.Column(db.Integer)
    smokers_count = db.Column(db.Integer)
    smokers_percent = db.Column(db.Numeric)
    veggie_count = db.Column(db.Integer)
    veggies_percent = db.Column(db.Numeric)
    fruit_count = db.Column(db.Integer)
    fruit_percent = db.Column(db.Numeric)
    overweight_BMI_count = db.Column(db.Integer)
    overweight_BMI_percent = db.Column(db.Numeric)
    obese_BMI_highschool_count = db.Column(db.Integer)
    obese_BMI_highschool_percent = db.Column(db.Numeric)
    obese_BMI_20_plus_count = db.Column(db.Integer)
    obese_BMI_20_plus_percent = db.Column(db.Numeric)
    healthy_BMI_20_plus_count = db.Column(db.Integer)
    healthy_BMI_20_plus_percent = db.Column(db.Numeric)
    no_physical_activity_count = db.Column(db.Integer)
    no_physical_activity_percent = db.Column(db.Numeric)

    def __repr__(self):
        return '<Cancer %r>' % (self.name)


# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()


##########################################################
 #                   The Routes
##########################################################

@app.route("/")
def main():
    return render_template("index.html")


@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/pie")
def pie():
    return render_template("state_pie.html")


@app.route("/top5incd")
def top5incd():
    return render_template("topfiveIncidence.html")


@app.route("/top5mort")
def top5mort():
    return render_template("topfiveMortality.html")


@app.route("/breastcancer")
def breast():
    return render_template("map_breast.html")


@app.route("/coloncancer")
def colon():
    return render_template("map_colon.html")

@app.route("/lungcancer")
def lung():
    return render_template("map_lung.html")

@app.route("/skincancer")
def skin():
    return render_template("map_skin.html")

@app.route("/prostatecancer")
def prostate():
    return render_template("map_prostate.html")



@app.route("/api/risks")
def stateriskdata():

    df = pd.read_sql_table("risk", "sqlite:///data/cancer.sqlite")
    df.set_index(['State'])
    data = []
    Dict = {}
    c = 0
    for i, row in df.iterrows():
        data.append({
            'State': row["State"],
            'Smoking %': row["smokers_percent"],
            'Veggies %' : row["veggies_percent"],
            'Fruit %' : row["fruit_percent"],
            'Overweight BMI %' : row["overweight_BMI_percent"],
            'Obese BMI highschool %' : row["obese_BMI_highschool_percent"],
            'Obese BMI age 20 plus %' : row["obese_BMI_20_plus_percent"],
            'Healthy BMI age 20 plus %' : row["healthy_BMI_20_plus_percent"],
            'No physical activity %' : row["no_physical_activity_percent"]
        })

    return jsonify(data)


@app.route("/api/riskscolumns")
def staterisks():
    """Return a list of sample names."""
    # Use Pandas to perform the sql query
    stmt = db.session.query(risk_data).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[:])


@app.route("/api/census")
def census():

    census_df = pd.read_sql_table("census", "sqlite:///data/cancer.sqlite")
    census_df.set_index(['State'])
    c_data = []
    Dict = {}
    c = 0

    for i, row in census_df.iterrows():
        c_data.append({
            'State': row["State"],
            'Crowding %': row["crowding_percent"],
            '% With Bachelors': row["education_bachelors_percent"],
            'Median Family Income': row["median_family_income_dollars"],
            'Uninsured %': row["uninsured_percent"],
            '>150 Poverty %': row["below_150_poverty_percent"],
            'Unemployed %': row["unemployed_percent"]
        })

    return jsonify(c_data)

@app.route("/api/incidencecolumns")
def incidencecolumns():
    """Return a list of sample names."""
    # Use Pandas to perform the sql query
    stmt = db.session.query(cancer_data).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[:])

@app.route("/api/incidence")
def incidence():

    # Query all cancers counts
    results = db.session.query(cancer_data.State, cancer_data.bladder_count, 
        cancer_data.brain_count, cancer_data.breast_count, cancer_data.cervix_count,
        cancer_data.colon_rectum_count, cancer_data.esophagus_count,
        cancer_data.kidney_count, cancer_data.leukemia_count, cancer_data.liver_count, cancer_data.lung_count, 
        cancer_data.melanoma_count, cancer_data.non_HodgkinL_count,
        cancer_data.oral_pharynx_count, cancer_data.ovary_count, cancer_data.pancreas_count, cancer_data.prostate_count,
        cancer_data.stomach_count, cancer_data.thyroid_count, cancer_data.uterus_count).all()

    # Create a dictionary from the row data and append to a list of all_passengers
    cancer_counts = []
    for State, bladder_count, brain_count, breast_count, cervix_count, colon_rectum_count, esophagus_count, kidney_count, leukemia_count, liver_count, lung_count, melanoma_count, non_HodgkinL_count, oral_pharynx_count, ovary_count, pancreas_count, prostate_count, stomach_count, thyroid_count, uterus_count in results:
        cancer_dict = {}
        cancer_dict["State"] = State
        cancer_dict["Bladder cancer incidence"] = bladder_count
        cancer_dict["Brain cancer incidence"] = brain_count
        cancer_dict["Breast cancer incidence"] = breast_count
        cancer_dict["Cervix cancer incidence"] = cervix_count
        cancer_dict["colon rectum cancer incidence"] = colon_rectum_count
        cancer_dict["Esophagus cancer incidence"] = esophagus_count
        cancer_dict["Kidney cancer incidence"] = kidney_count
        cancer_dict["Leukemia cancer incidence"] = leukemia_count
        cancer_dict["Liver cancer incidence"] = liver_count
        cancer_dict["Lung cancer incidence"] = lung_count
        cancer_dict["Melanoma cancer incidence"] = melanoma_count
        cancer_dict["NonHodgkinL cancer incidence"] = non_HodgkinL_count
        cancer_dict["Oral Pharynx cancer incidence"] = oral_pharynx_count
        cancer_dict["Ovary cancer incidence"] = ovary_count
        cancer_dict["Pancreas cancer incidence"] = pancreas_count
        cancer_dict["Prostate cancer incidence"] = prostate_count
        cancer_dict["Stomach cancer incidence"] = stomach_count
        cancer_dict["Thyroid cancer incidence"] = thyroid_count
        cancer_dict["Uterus cancer incidence"] = uterus_count
        cancer_counts.append(cancer_dict)

    return jsonify(cancer_counts)

@app.route("/api/mortality")
def mortality():

    # Query all cancers counts
    results = db.session.query(death_data.State, death_data.bladder_count, 
    	death_data.brain_count, death_data.breast_count, death_data.cervix_count,
    	death_data.colon_rectum_count, death_data.esophagus_count,
    	death_data.kidney_count, death_data.leukemia_count, death_data.liver_count, death_data.lung_count, 
    	death_data.melanoma_count, death_data.nonHodgkinL_count,
    	death_data.oral_pharynx_count, death_data.ovary_count, death_data.pancreas_count, death_data.prostate_count,
    	death_data.stomach_count, death_data.thyroid_count, death_data.uterus_count).all()

    # Create a dictionary from the row data and append to a list of all_passengers
    death_counts = []

    for State, bladder_count, brain_count, breast_count, breastinsitu_count, cervix_count, colon_rectum_count, esophagus_count, kidney_count, leukemia_count, liver_count, lung_count, melanoma_count, nonHodgkinL_count, oral_pharynx_count, ovary_count, pancreas_count, prostate_count, stomach_count, thyroid_count, uterus_count in results:
        death_dict = {}
        death_dict["State"] = State
        death_dict["Bladder cancer incidence"] = bladder_count
        death_dict["Brain cancer incidence"] = brain_count
        death_dict["Breast cancer incidence"] = breast_count
        death_dict["Breastinsitu cancer incidence"] = breastinsitu_count
        death_dict["Cervix cancer incidence"] = cervix_count
        death_dict["colon rectum cancer incidence"] = colon_rectum_count
        death_dict["Esophagus cancer incidence"] = esophagus_count
        death_dict["Kidney cancer incidence"] = kidney_count
        death_dict["Leukemia cancer incidence"] = leukemia_count
        death_dict["Liver cancer incidence"] = liver_count
        death_dict["Lung cancer incidence"] = lung_count
        death_dict["Melanoma cancer incidence"] = melanoma_count
        death_dict["NonHodgkinL cancer incidence"] = nonHodgkinL_count
        death_dict["Oral Pharynx cancer incidence"] = oral_pharynx_count
        death_dict["Ovary cancer incidence"] = ovary_count
        death_dict["Pancreas cancer incidence"] = pancreas_count
        death_dict["Prostate cancer incidence"] = prostate_count
        death_dict["Stomach cancer incidence"] = stomach_count
        death_dict["Thyroid cancer incidence"] = thyroid_count
        death_dict["Uterus cancer incidence"] = uterus_count
        death_counts.append(death_dict)

    return jsonify(death_counts)

@app.route("/gz_2010_us_040_00_20m")
def state_outlines():
    filename = os.path.join(app.static_folder, 'gz_2010_us_040_00_20m.json')
    with open(filename) as jsonfile:
        data = json.load(jsonfile)

    return jsonify(data)


from flask import request
from flask import send_file

@app.route('/image1')
def get_image1():
    if request.args.get('type') == '1':
       filename = 'templates\images\image1.jpg'
    else:
       filename = 'templates\images\image1.jpg'
    return send_file(filename, mimetype='image/gif')

@app.route('/image2')
def get_image2():
    if request.args.get('type') == '1':
       filename = 'templates\images\image2.jpg'
    else:
       filename = 'templates\images\image2.jpg'
    return send_file(filename, mimetype='image/gif')

@app.route('/image3')
def get_image3():
    if request.args.get('type') == '1':
       filename = 'templates\images\image3.jpeg'
    else:
       filename = 'templates\images\image3.jpeg'
    return send_file(filename, mimetype='image/gif')


if __name__ == "__main__":
    app.run()
