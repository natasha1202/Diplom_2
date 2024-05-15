import string
import random

import allure
import requests

from api_url import ApiUrl


class Helper:

    @allure.step('Генерация произвольной строки')
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @allure.step('Удаление созданного пользователя')
    def delete_user(self, user):
        token = self.login_as_user(user)
        headers = {"Authorization": token}
        requests.delete(ApiUrl.DELETE_USER_URL, headers=headers)

    @allure.step('Авторизация пользователя')
    def login_as_user(self, login_data):
        response = requests.post(ApiUrl.AUTH_USER_URL, data=login_data)
        access_token = response.json()['accessToken']
        return access_token

    @allure.step('Замена значения поля на пустое')
    def exclude_parameter(self, user, condition):
        if condition == "no_email":
            user['email'] = None
        elif condition == "no_password":
            user['password'] = None
        elif condition == "no_name":
            user['name'] = None
        return user

    @allure.step('Замена значения поля на несуществующее')
    def change_to_wrong_parameter(self, user, condition):
        if condition == "wrong_email":
            user['email'] = "abc"
        elif condition == "wrong_password":
            user['password'] = "123"
        return user

    @allure.step('Генерация нового значения поля')
    def update_data(self, user, condition):
        if condition == "email":
            user['email'] = f'k52{self.generate_random_string(8)}@ya.ru'
        elif condition == "password":
            user['password'] = self.generate_random_string(10)
        elif condition == "name":
            user['name'] = self.generate_random_string(14)
        return user




