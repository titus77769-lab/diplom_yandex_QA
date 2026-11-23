import data
import sender_stand_request


def test_ping():
    response = sender_stand_request.check_ping()
    assert response.status_code == 200
    assert "pong" in response.text


def test_track():
    create = sender_stand_request.send_order(data.order_data)
    assert create.status_code == 201

    track = create.json()["track"]
    assert track

    get = sender_stand_request.get_track(track)
    assert get.status_code == 200

    order = get.json().get("order")
    assert order is not None
    assert order["track"] == track