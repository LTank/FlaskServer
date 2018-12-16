import json
import requests


def get_all_messages():
    djson = requests.get('http://localhost:9000/api/messages')
    json_dict = json.loads(djson.content.decode())
    msgs = json_dict.get('msgs')
    print('API call: GET /messages')
    return msgs


def get_user(usr_name, usr_pswd):
    response = requests.get('http://localhost:9000/api/user/' + usr_name +'?p=' + usr_pswd)
    dict = json.loads(response.content.decode())
    print('API call: GET /user/' + usr_name +'?p=' + usr_pswd)
    if bool(dict):
        return dict.get('usr_id')
    else:
        return None


def create_user(json):
    print('API call: POST /user')
    return requests.post('http://localhost:9000/api/user', data=None, json=json)


def post_message(json):
    print('API call: POST /messages')
    return requests.post('http://localhost:9000/api/messages', data=None, json=json)

