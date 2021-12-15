from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
#db = SQLAlchemy(app)

@app.route('/')
def home():
    return f"Hello ARG PAINS! {os.getenv('connectionstring')}"
    
    #render_template('index.html') 
    #f"Hello Automated Deployment! This is built originally on {platform.node()}"

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)