from flask import Flask
import platform

app = Flask(__name__)

@app.route('/')
def home():
    return f"Hello Automated Deployment! This is built originally on {platform.node()}"

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)