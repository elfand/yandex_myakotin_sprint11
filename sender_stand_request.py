import configuration
import requests
import data


def post_new_order():
    order_track = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,  # подставляем полный url
                          headers=data.headers)  # а здесь заголовки

    return order_track.json()["track"]


def check_info_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.STATUS_ORDER + track,  # подставляем полный url
                          headers=data.headers) # возвращаем сразу весь ответ

