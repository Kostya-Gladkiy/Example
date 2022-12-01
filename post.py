import requests


url = "http://127.0.0.1:8000/add_user"


def get_data():
    data = {
        "first_name": None,
        "last_name": None,
        "email": None,
        "age": None
    }
    for key in data:
        value = input(key+": ")
        data[key] = value
    return data


def send_data(data: dict = {}):
    resp = requests.post(url, json=data)
    print("Result: "+resp.text)


while True:
    data = get_data()
    if data:
        send_data(data)
