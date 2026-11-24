import pytest

import data
import sender_stand_request


@pytest.fixture
def order_response():
    """Готовит ответ на создание заказа, без проверок в теле фикстуры."""
    return sender_stand_request.send_order(data.order_data)


@pytest.fixture
def created_order_track(order_response):
    """Готовит трек созданного заказа для тестов на получение."""
    assert order_response.status_code == 201, (
        f"Не удалось создать заказ для теста: {order_response.status_code}. "
        f"Ответ: {order_response.text}"
    )
    track = order_response.json().get("track")
    assert track, "В ответе на создание заказа отсутствует track"
    return track


def test_create_order_returns_201(order_response):
    assert order_response.status_code == 201


def test_create_order_contains_track(order_response):
    assert order_response.json().get("track") is not None


def test_get_order_by_track_returns_200(created_order_track):
    response = sender_stand_request.get_track(created_order_track)
    assert response.status_code == 200


def test_get_order_by_track_returns_correct_order(created_order_track):
    response = sender_stand_request.get_track(created_order_track)
    order = response.json().get("order", {})
    assert order.get("track") == created_order_track


def test_ping_returns_200():
    response = sender_stand_request.check_ping()
    assert response.status_code == 200


def test_ping_returns_pong():
    response = sender_stand_request.check_ping()
    assert "pong" in response.text