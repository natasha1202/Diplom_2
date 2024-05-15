from copy import deepcopy

import allure
import pytest
import requests

from api_url import ApiUrl
from data import Data
from helpful_classes.assertions import Assertions
from helpful_classes.helper import Helper


@allure.epic("Логин пользователя")
class TestLogin:

    @allure.title('Логин пользователя. Позитивный сценарий')
    @allure.description('Существующий пользователь успешно авторищуется в системе. '
                        'Проверяется корректность кода ответа и сообщения об успехе')
    def test_login_success(self, registered_user):
        response = requests.post(ApiUrl.AUTH_USER_URL, data=registered_user)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_value_by_name(
            response, 'success', True, Data.ASSERTIONS_INCORRECT_FILED_ERROR_MESSAGE)

    @allure.title('Авторизация пользователя. Негативный сценарий. Одно из полей заполнено неверно. ')
    @allure.description('Авторизация пользователя не происходит, т.к. логин или пароль заполнены неверно. '
                        'Проверяется корректность кода ответа и сообщения об ошибке')
    @pytest.mark.parametrize("condition", [
        ("wrong_email"),
        ("wrong_password")
    ])
    def test_login_mandatory_field_incorrect(self, condition, registered_user):
        new_user = deepcopy(registered_user)
        helper = Helper()
        new_data = helper.change_to_wrong_parameter(new_user, condition)

        response = requests.post(ApiUrl.AUTH_USER_URL, data=new_data)
        Assertions.assert_code_status(response, 401)
        Assertions.assert_json_value_by_name(
            response,
            'message',
            Data.INCORRECT_CREDENTIALS_ERROR_MESSAGE,
            Data.ASSERTIONS_ERROR_MESSAGE)
