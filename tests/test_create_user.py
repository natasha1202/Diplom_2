import allure
import pytest
import requests

from api_url import ApiUrl
from helpful_classes.assertions import Assertions
from helpful_classes.helper import Helper
from helpful_classes.user_generator import UserGenerator


@allure.epic("Создание нового пользователя")
class TestCreateUser:

    @allure.title('Создание пользователя. Позитивный сценарий')
    @allure.description('Успешное создание нового пользователя в системе. '
                        'Проверяется корректность кода ответа и сообщения об успехе')
    def test_create_new_user_success(self):
        user = UserGenerator.create_new_user_and_return_login_password()

        response = requests.post(ApiUrl.CREATE_USER_URL, data=user)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_value_by_name(
            response, 'success', True, 'Success field has incorrect value')

        Helper.delete_user(user)

    exclude_params = [
        ("no_email"),
        ("no_password"),
        ("no_name")
    ]

    @allure.title('Создание пользователя. Негативный сценарий. Одно из полей не заполнено. ')
    @allure.description('Создание нового пользователя не происходит, т.к. не заполнено одно из обязательных полей. '
                        'Проверяется корректность кода ответа и сообщения об ошибке')
    @pytest.mark.parametrize("condition", exclude_params)
    def test_create_user_mandatory_field_missed(self, condition):
        user = UserGenerator.create_new_user_and_return_login_password()
        Helper.exclude_parameter(user, condition)

        response = requests.post(ApiUrl.CREATE_USER_URL, data=user)
        Assertions.assert_code_status(response, 403)
        Assertions.assert_json_value_by_name(
            response,
            'message',
            'Email, password and name are required fields',
            'Error message is incorrect')

    @allure.title('Создание пользователя. Негативный сценарий. Попытка повторного создания существующего клиента. ')
    @allure.description('Создание нового пользователя не происходит, пользователь уже существует. '
                        'Проверяется корректность кода ответа и сообщения об ошибке')
    def test_create_user_already_exist(self):
        user = UserGenerator.register_new_user_and_return_login_password()

        response = requests.post(ApiUrl.CREATE_USER_URL, data=user)

        Assertions.assert_code_status(response, 403)
        Assertions.assert_json_value_by_name(
            response,
            'message',
            'User already exists',
            'Error message is incorrect')

        Helper.delete_user(user)





