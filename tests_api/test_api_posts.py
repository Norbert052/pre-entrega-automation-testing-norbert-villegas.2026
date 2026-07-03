import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


@pytest.mark.api
def test_get_post_by_id():
    response = requests.get(f"{BASE_URL}/posts/1", timeout=TIMEOUT)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)

    expected_keys = ["userId", "id", "title", "body"]
    for key in expected_keys:
        assert key in data, f"Response JSON should contain '{key}'"

    assert isinstance(data["userId"], int)
    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)
    assert data["id"] == 1


@pytest.mark.api
def test_create_post():
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload, timeout=TIMEOUT)
    assert response.status_code == 201

    data = response.json()
    assert isinstance(data, dict)
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data
    assert isinstance(data["id"], int)


@pytest.mark.api
def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1", timeout=TIMEOUT)
    assert response.status_code in (200, 204)
    assert response.text == "" or response.text == "{}"
