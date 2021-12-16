from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import DataRequired
from wtforms.widgets.core import Select

### Initialisation                 ######################


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://squid@flaskdb:flaskappoctopus123!@flaskdb.mysql.database.azure.com:3306/appdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'TOTALLYSECRETKEY'
db = SQLAlchemy(app)

###                                ######################



### Defining database layer schema ######################

class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    servicename = db.Column(db.String(40), nullable=False)
    company = db.Column(db.String(40), nullable=False)
    isCompromised = db.Column(db.Integer, nullable=False)
    agency = db.relationship('Agencies', backref='service')

class Agencies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agencyname = db.Column(db.String(40), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)

###                                ######################


### Defining Forms                 ######################

class CreateServiceForm(FlaskForm):
    servicename = StringField('Service Name', validators=[DataRequired()])
    company = StringField('Company Name', validators=[DataRequired()])
    isCompromised = SelectField("Compromised Status - True or False", choices=[(1,'True'),(0,'False')], validators=[DataRequired()])
    submit = SubmitField('Add Service')

class CreateAgencyForm(FlaskForm):
    agencyname = StringField('Agency Name', validators=[DataRequired()])
    service_id = StringField('Service ID - from Services list. Leave empty if no map to an Internet service.')
    submit = SubmitField('Add Agency')



###                                ######################



### Defining routes                ######################

@app.route('/')
def home():
    #return f"Hello PAINNEW14! {os.getenv('connectionstring')}"
    return render_template('index.html') 

@app.route('/create', methods=['GET', 'POST'])
def create():

    message = ''
    secondmessage = ''
    form = CreateServiceForm()
    secondform = CreateAgencyForm()

    if request.method == 'POST':
        servicename = form.servicename.data
        company = form.company.data
        isCompromised = form.isCompromised.data

        agencyname = secondform.agencyname.data
        service_id = secondform.service_id.data

        if len(str(servicename)) == 0 or len(str(company)) == 0:
            message = "Please ensure that the fields are entered in."
        else:
            message = f"Added service: {servicename} {company} {isCompromised}"
        
        if len(str(agencyname)) == 0:
            secondmessage = "Please ensure that the agency field is filled in. "
        else:
            secondmessage = f"Added agency {agencyname}, mapped to service: {service_id}"

        if form.validate_on_submit():
            service = Services(servicename=servicename, company=company, isCompromised=isCompromised)
            db.session.add(service)
            db.session.commit()
        
        if secondform.validate_on_submit():
            agency = Agencies(agencyname=agencyname, service_id=service_id)
            db.session.add(agency)
            db.session.commit()


    return render_template('create.html', form=form, message=message, secondform=secondform, secondmessage=secondmessage) 

@app.route('/read')
def read():
    return render_template('read.html') 

@app.route('/update')
def update():
    return render_template('update.html') 

@app.route('/delete')
def delete():
    return render_template('delete.html') 

###                                ######################




### Running the application        ######################


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

###                                ######################