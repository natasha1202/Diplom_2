from copy import deepcopy

import allure
import pytest
import requests

from api_url import ApiUrl
from helpful_classes.assertions import Assertions
from helpful_classes.helper import Helper
from helpful_classes.user_generator import UserGenerator


@allure.epic("Логин пользователя")
class TestLogin:

    @allure.title('Логин пользователя. Позитивный сценарий')
    @allure.description('Существующий пользователь успешно авторищуется в системе. '
                        'Проверяется корректность кода ответа и сообщения об успехе')
    def test_login_success(self):
        user = UserGenerator.register_new_user_and_return_login_password()
        response = requests.post(ApiUrl.AUTH_USER_URL, data=user)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_value_by_name(
            response, 'success', True, 'Success field has incorrect value')

        Helper.delete_user(user)

    exclude_params = [
        ("wrong_email"),
        ("wrong_password")
        ]

    @allure.title('Авторизация пользователя. Негативный сценарий. Одно из полей заполнено неверно. ')
    @allure.description('Авторизация пользователя не происходит, т.к. логин или пароль заполнены неверно. '
                        'Проверяется корректность кода ответа и сообщения об ошибке')
    @pytest.mark.parametrize("condition", exclude_params)
    def test_login_mandatory_field_incorrect(self, condition):
        registered_user = UserGenerator.register_new_user_and_return_login_password()
        user = deepcopy(registered_user)
        new_data = Helper.change_to_wrong_parameter(registered_user, condition)

        response = requests.post(ApiUrl.AUTH_USER_URL, data=new_data)
        Assertions.assert_code_status(response, 401)
        Assertions.assert_json_value_by_name(
            response,
            'message',
            'email or password are incorrect',
            'Error message is incorrect')

        Helper.delete_user(user)


