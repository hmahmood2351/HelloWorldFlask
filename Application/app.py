from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello_internet():
    return f"Hello Automated Deployment! This is built originally on {socket.gethostname()}"

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)