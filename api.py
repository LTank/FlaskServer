import json
import requests


class Api:
    def __init__(self, usr_id, json):
        self.getAllMessages = get_all_messages()
        self.getUserById = get_user_by_id(usr_id)
        self.createUser = create_user(json)
        self.postMessage = post_message(json)


def get_all_messages():
    djson = requests.get('http://localhost:9000/api/massages')
    json_dict = json.loads(djson.content.decode())
    msgs = json_dict.get('msgs')
    return msgs


def get_user_by_id(usr_id):
    djson = requests.get('http://localhost:9000/api/user/' + usr_id)
    json_dict = json.loads(djson.content.decode())
    u_id = json_dict.get('usr_id')
    return u_id


def create_user(json):
    djson = requests.post('http://localhost:9000/api/user', data=None, json=json)
    return 1


def post_message(json):
    djson = requests.post('http://localhost:9000/api/messages', data=None, json=json)
    return 1
