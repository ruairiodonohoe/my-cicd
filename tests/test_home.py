"""Tests for home."""

from http import HTTPStatus

from my_cicd.app import app


def test_home() -> None:
    """Tests home function."""
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.data.decode() == "Home again"
