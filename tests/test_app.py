import io

from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Docker Container Topology Visualizer" in response.data


def test_upload_valid_compose_file():
    client = app.test_client()

    compose_file = """
services:
  web:
    image: nginx
    depends_on:
      - db

  db:
    image: postgres
"""

    response = client.post(
        "/api/parse",
        data={
            "file": (
                io.BytesIO(compose_file.encode()),
                "docker-compose.yml"
            )
        },
        content_type="multipart/form-data"
    )

    data = response.get_json()

    assert response.status_code == 200
    assert data["success"] is True
    assert "web" in data["services"]
    assert "db" in data["services"]
    assert len(data["graph"]["nodes"]) == 2
    assert len(data["graph"]["edges"]) == 1


def test_upload_without_file():
    client = app.test_client()

    response = client.post("/api/parse")

    data = response.get_json()

    assert response.status_code == 400
    assert data["success"] is False


def test_upload_invalid_compose_file():
    client = app.test_client()

    invalid_file = """
hello: world
"""

    response = client.post(
        "/api/parse",
        data={
            "file": (
                io.BytesIO(invalid_file.encode()),
                "invalid.yml"
            )
        },
        content_type="multipart/form-data"
    )

    data = response.get_json()

    assert response.status_code == 400
    assert data["success"] is False
    assert "services" in data["error"]