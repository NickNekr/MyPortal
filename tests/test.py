import requests
from config import Config

#Лайк за тесты. У меня их, к примеру, нет. Совсем...
def test_hello_world():
    response = requests.get(f"{Config.BASE_URL}/")
    assert response.text == "<p>Hello, DIT!</p>"
    assert response.status_code == Config.ResponseStatusCode.OK


def test_add_and_delete_user():
    response = requests.post(f"{Config.BASE_URL}/1/Kolya")
    assert response.text == "<p>User found!</p>"
    assert response.status_code == Config.ResponseStatusCode.OK

    response = requests.get(f"{Config.BASE_URL}/1")
    assert response.json() == {"id": 1,
                               "username": "Kolya"}
    assert response.status_code == Config.ResponseStatusCode.OK

    response = requests.post(f"{Config.BASE_URL}/1/Kolya")
    assert response.text == "<p>The user already exists!</p>"
    assert response.status_code == Config.ResponseStatusCode.BAD_REQUEST

    response = requests.delete(f"{Config.BASE_URL}/1")
    assert response.text == "<p>User was deleted!</p>"
    assert response.status_code == Config.ResponseStatusCode.OK

    response = requests.delete(f"{Config.BASE_URL}/2")
    assert response.text == "<p>User not found!</p>"
    assert response.status_code == Config.ResponseStatusCode.NOT_FOUND
