from app import app
import flask
from flask import Flask, jsonify, request
import requests
from requests import post
import json

@app.route('/posting', methods=['POST'])
def posting():

    def send_json1(sendjson1):
        sendjson1 = post("http://127.0.0.1:5002/set_department", json=sendjson1, headers={"Content-type": "application/json"})
        print(sendjson1.text)
    def send_json2(sendjson2):
        sendjson2 = post("http://127.0.0.1:5002/set_team", json=sendjson2, headers={"Content-type": "application/json"})
        print(sendjson2.text)
    def send_json3(sendjson3):
        sendjson3 = post("http://127.0.0.1:5002/set_employee", json=sendjson3, headers={"Content-type": "application/json"})
        print(sendjson3.text)

    datajson = request.data
    data = json.loads(datajson)

    for i in data:
        if i == "department":
            Department = data["department"]
            if Department == None:
                pass
            else:
                send_json1(Department)
        elif i == "team":
            Team = data["team"]
            if Team == None:
                pass
            else:
                send_json2(Team)
        elif i == "employee":
            Employee = data["employee"]
            if Employee == None:
                pass
            else:
                send_json3(Employee)
        else:
            pass
            
    return ""
