import configuration
import requests
import data

# Создание нового заказа
def post_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)
order_track = post_order(data.order_body).json()["track"]


# Получение данных о заказе по треку api/v1/orders/track?t=220307
def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.TAKE_ORDER_BY_TRACK + str(track))



