from flask import Flask
import flask
import json
import requests
import os

app = Flask(__name__)



URL_DEP = str(os.getenv("URL_DB")) + 'get-dep'
URL_EMPL = str(os.getenv("URL_DB")) + 'get-empl'
URL_TEAM = str(os.getenv("URL_DB")) + 'get-team'
URL_ALL = str(os.getenv("URL_DB")) + 'get-info'

def print_url():
    print(URL_DEP)
    print(URL_TEAM)
    print(URL_EMPL)
    

def get_dep():
    r = requests.get(URL_DEP)
    if r.status_code == 200:
        return r.content
    else:
        return (r.status_code, r.headers)

def get_empl():
    re = requests.get(URL_EMPL)
    if re.status_code == 200:
        return re.content
    else:
        return (re.status_code, re.headers)


def get_team():
    req = requests.get(URL_TEAM)
    if req.status_code == 200:
        return req.content
    else:
        return (req.status_code, req.headers)


def parse_json(arg1, arg2, arg3):
    dictionary = {}
    dictionary = {**arg1, **arg2, **arg3}
    return json.dumps(dictionary)

#Employee

def salary_employee(dict_emp):
    for i in dict_emp['Employee']:
        if int(i['exp']) > 2 and int(i['exp']) < 5:
            i['salary'] = int(int(i['salary']) + 200)
        elif i['exp'] > 5:
            i['salary'] = int(int(i['salary'])*1.2 +  500)
        else:
            pass


#Manager
def salary_manager(dict_team, dict_emp):
    count = 0
    for i in dict_team['Team']:
        for j in dict_emp['Employee']:
            if j['position'] != "Manager" and j['team_id'] == i['team_id']:
                count += 1
        for k in dict_emp['Employee']:
            if count > 5 and dict_emp['Employee']['position'] == 'Manager' and k['team_id'] == i['team_id']:
                k['salary'] += 200
            elif count > 10 and dict_emp['Employee']['position'] == 'Manager' and k['team_id'] == i['team_id']:
                k['salary'] += 300
            elif count_dev(dict_team, dict_emp) > count / 2 and k['position'] == 'Manager' and k['team_id'] == i['team_id']:
                k['salary'] = int(int(k['salary'])*1.1)
            else:
                pass

def count_dev(dict_team, dict_emp):
    count = 0
    for i in dict_team['Team']:
        for j in dict_emp['Employee']:
            if j['position'] == 'Developer':
                count += 1
            else:
                pass
    return count

#Designer

def salary_designer(dict_emp):
    for i in dict_emp['Employee']:
        if i['position'] == "Designer":
            i['salary'] = int(int(i['salary'])*i['coefficient'])
        else:
            pass


@app.route('/get', methods=['GET'])
def get_info():
    print_url()
    #print("GOOOOOD")
    #req = requests.get(URL_ALL)
    #return json.dumps(req)
    return URL_DEP + "!!!!!!!!!"

@app.route('/get-one', methods=['GET'])
def get_one():
    emp = get_empl()
    team = get_team()
    dep = get_dep()
    dep = json.loads(dep)
    emp = json.loads(emp)
    team = json.loads(team)
    salary_designer(emp)
    salary_employee(emp)
    salary_manager(team, emp)
    res = parse_json(dep, team, emp)
    #res = {'name':'text'}
    return res


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='5003')

