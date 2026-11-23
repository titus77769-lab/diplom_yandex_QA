import requests

import configuration
import data


def send_order(payload):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=payload,
        headers=data.headers
    )


def get_track(track):
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
        params={"t": track},
        headers=data.headers
    )


def check_ping():
    return requests.get(configuration.URL_SERVICE + configuration.PING_PATH)