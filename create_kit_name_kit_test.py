import sender_stand_request
import data


def get_kit_body(kit_body):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.kits_data.copy()
    # изменение значения в поле name
    current_body["name"] = kit_body
    # возвращается новый словарь с нужным значением name
    return current_body


def positive_assert(name):
    # В переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
    # В переменную Token сохраняется результат запроса на создание пользователя, его токен:
    token = sender_stand_request.post_new_user(data.user_body)
    # В переменную user_response сохраняется результат запроса на создание набора:
    user_response = sender_stand_request.post_new_client_kit(kit_body, token)

    # Проверяется, что код ответа равен 201
    assert user_response.status_code == 201
    # Проверяется, что в ответе есть поле name, и оно равно тому name которое отправляется в тесте
    assert user_response.json()["name"] == kit_body["name"]



def negative_assert(name):
    # В переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
    # В переменную Token сохраняется результат запроса на создание пользователя, его токен:
    token = sender_stand_request.post_new_user(data.user_body)
    # В переменную user_response сохраняется результат запроса на создание набора:
    user_response = sender_stand_request.post_new_client_kit(kit_body, token)

    # Проверяется, что код ответа равен 400
    assert user_response.status_code == 400
    # Проверяем что в ответе есть JSON и в нем есть ключ code с верным кодом ошибки
    assert user_response.json()["code"] == 400


def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("A")


def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


def test_create_kit_0_letter_in__name_get_failed_response():
    negative_assert("")


def test_create_kit_512_letter_in__name_get_failed_response():
    negative_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


def test_create_kit_ENG_letter_in_name_get_success_response():
    positive_assert("QWErty")


def test_create_kit_RU_letter_in_name_get_success_response():
    positive_assert("Мария")


def test_create_kit_SYMBOL_letter_in_name_get_success_response():
    positive_assert(r'"№%@",')


def test_create_kit_SPACE_letter_in_name_get_success_response():
    positive_assert(" Человек и КО ")


def test_create_kit_NUMBERS_letter_in_name_get_success_response():
    positive_assert("123")


def negative_assert_with_no_body(kit_body):
    # Объявляем переменную с пустыми данными. На вход в функции тоже убираем параметры
    # kit_body = {}
    # В переменную Token сохраняется результат запроса на создание пользователя, его токен:
    token = sender_stand_request.post_new_user(data.user_body)
    # В переменную user_response сохраняется результат запроса на создание набора:
    user_response = sender_stand_request.post_new_client_kit(kit_body, token)

    # Проверяется, что код ответа равен 400
    assert user_response.status_code == 400
    # Проверяется, что в ответе есть поле authToken, и оно не пустое
    assert user_response.json()["code"] == 400


def test_create_kit_WITH_NO_BODY_get_failed_response():
    kit_body = {}
    negative_assert_with_no_body(kit_body)


def test_create_kit_ANOTHER_TYPE_get_failed_response():
    negative_assert(123)
