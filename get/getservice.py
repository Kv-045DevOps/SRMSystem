from flask import Flask
from app import routes

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='5003')
