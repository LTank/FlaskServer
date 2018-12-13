import json
import requests


def get_all_messages():
    djson = requests.get('http://localhost:9000/api/messages')
    json_dict = json.loads(djson.content.decode())
    msgs = json_dict.get('msgs')
    return msgs


def get_user(usr_name, usr_pswd):
    response = requests.get('http://localhost:9000/api/user/' + usr_name +'?p=' + usr_pswd)
    dict = json.loads(response.content.decode())
    if bool(dict):
        return dict.get('usr_id')
    else:
        return None

def create_user(json):
    djson = requests.post('http://localhost:9000/api/user', data=None, json=json)
    return 1


def post_message(json):
    return requests.post('http://localhost:9000/api/messages', data=None, json=json)

