import requests

def test_can_add_film():
    response = requests.request('GET', "http://restream-recom1.herokuapp.com/qa/movies")
    print(response.json())
    assert response.status_code == 200
    assert response.json()["items"][0]['name'] == "JoysFilm"
