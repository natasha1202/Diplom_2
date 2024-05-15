import allure
import requests

from api_url import ApiUrl
from helpful_classes.helper import Helper


class UserGenerator:

    @allure.step('Генерируется новый незарегистрированный пользователь')
    def create_new_user_and_return_login_password(self):
        helper = Helper()
        username = f'k5{helper.generate_random_string(10)}'
        email = f'{username}@ya.ru'
        password = helper.generate_random_string(10)

        return {"email": email, "password": password, "name": username}

    @allure.step('Генерируется новый зарегистрированный пользователь')
    def register_new_user_and_return_login_password(self):
        user = self.create_new_user_and_return_login_password()

        response = requests.post(ApiUrl.CREATE_USER_URL, data=user)
        if response.status_code == 200:
            return user

