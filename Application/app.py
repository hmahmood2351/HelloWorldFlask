from flask import Flask, render_template
import platform

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') 
    #f"Hello Automated Deployment! This is built originally on {platform.node()}"

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)