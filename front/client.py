import requests


def simple_api_call():
    response = requests.post("http://localhost:8000/the/endpoint/path", json={"key": "value"})
    return response.json()


if __name__ == "__main__":

    simple_api_call()
