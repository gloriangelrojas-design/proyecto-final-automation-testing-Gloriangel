import requests


def test_get_posts():

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0
    assert isinstance(data, list)


def test_get_post_by_id():

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == 1
    assert "title" in body


def test_delete_post():

    response = requests.delete(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    assert response.status_code in [200, 204]