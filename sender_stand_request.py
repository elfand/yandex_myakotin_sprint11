import configuration
import requests
import data


def post_new_user(body):
    token = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                          json=body,  # тут тело
                          headers=data.headers)  # а здесь заголовки
    return token.json()["authToken"]


response = post_new_user(data.user_body);
print(response)

def post_new_client_kit(kit_body, auth_token):
    headers_copy = data.headers.copy()
    headers_copy["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.MAIN_KITS,  # подставляем полный url
                         json=kit_body,  # тут тело
                         headers=headers_copy)  # а здесь заголовки.

#response = post_new_client_kit(data.kits_data, "5c669615-c2c3-43c6-aecd-4bf6619a5194");
#print(response.status_code)
#print(response.json())
