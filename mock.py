import json

s = {
    "msgs": [
        {
            "msg_id": 1,
            "msg_text": "",
            "user_id": 1,
            "user_name": "qwe"
        },
        {
            "msg_id": 2,
            "msg_text": "",
            "user_id": 2,
            "user_name": "asd"
        },
        {
            "msg_id": 3,
            "msg_text": "",
            "user_id": 3,
            "user_name": "zxc"
        },
        {
            "msg_id": 4,
            "msg_text": "",
            "user_id": 4,
            "user_name": "dfg"
        }
    ]
}
jsonstr = json.dumps(s)
