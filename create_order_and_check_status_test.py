import sender_stand_request

# Мякотин Илья, 9-я когорта — Финальный проект. Инженер по тестированию плюс

def create_new_order():
    track = sender_stand_request.post_new_order() #Получаем трек номер заказа
    response = sender_stand_request.check_info_order(str(track)) # Отправялем запрос по данному трек номеру заказ

    assert response.status_code == 200 # Проверяем что код ответа 200



def test_create_order_and_status_true():
    create_new_order() # вызываем тест нашей функции

