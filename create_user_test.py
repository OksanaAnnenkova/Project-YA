# Оксана Анненкова, 10-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

# 1.Запрос на создание заказа
def test_create_order():
    response = sender_stand_request.post_order(data.order_body)
    assert response.status_code == 201


# 2.Сохранить номер трека заказа
def test_save_order_track():
    order_track = sender_stand_request.post_order(data.order_body).json()["track"]
    return order_track


# 3.Запрос на получения заказа по треку заказа
def test_take_order_by_orders_track():
    response = sender_stand_request.get_order(sender_stand_request.order_track)
    # Проверить, что код ответа равен 200
    assert response.status_code == 200