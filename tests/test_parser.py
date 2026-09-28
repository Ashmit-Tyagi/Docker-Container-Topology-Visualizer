import pytest

from src.parser import parse_compose_file


def test_parse_compose_file():
    services = parse_compose_file("sample/docker-compose.yml")

    assert "web" in services
    assert "backend" in services
    assert "db" in services


def test_service_information():
    services = parse_compose_file("sample/docker-compose.yml")

    assert services["web"]["image"] == "nginx"
    assert services["web"]["ports"] == ["80:80"]
    assert services["web"]["depends_on"] == ["backend"]


def test_missing_services(tmp_path):
    file = tmp_path / "invalid.yml"
    file.write_text("version: '3'")

    with pytest.raises(ValueError):
        parse_compose_file(file)


def test_empty_file(tmp_path):
    file = tmp_path / "empty.yml"
    file.write_text("")

    with pytest.raises(ValueError):
        parse_compose_file(file)