from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_list_courses():
    response = client.get("/courses")
    assert response.status_code == 200
    assert len(response.json()) == 6


def test_get_course():
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Python Basics"


def test_course_not_found():
    response = client.get("/courses/999")
    assert response.status_code == 404


def test_elective_filter():
    response = client.get("/courses?is_elective=true")
    assert response.status_code == 200
    assert all(course["is_elective"] for course in response.json())
