import allure
import requests

from api_url import ApiUrl
from helpful_classes.helper import Helper


class UserGenerator:

    @staticmethod
    @allure.step('Генерируется новый незарегистрированный пользователь')
    def create_new_user_and_return_login_password():
        username = f'k5{Helper.generate_random_string(10)}'
        email = f'{username}@ya.ru'
        password = Helper.generate_random_string(10)

        payload = {
            "email": email,
            "password": password,
            "name": username
        }
        return payload

    @staticmethod
    @allure.step('Генерируется новый зарегистрированный пользователь')
    def register_new_user_and_return_login_password():
        user = UserGenerator.create_new_user_and_return_login_password()

        response = requests.post(ApiUrl.CREATE_USER_URL, data=user)
        if response.status_code == 200:
            return user

