import allure
import pytest
import requests

from api_url import ApiUrl
from data import Data
from helpful_classes.assertions import Assertions
from helpful_classes.helper import Helper


@allure.epic("Создание нового пользователя")
class TestCreateUser:

    @allure.title('Создание пользователя. Позитивный сценарий')
    @allure.description('Успешное создание нового пользователя в системе. '
                        'Проверяется корректность кода ответа и сообщения об успехе')
    def test_create_new_user_success(self, user):
        response = requests.post(ApiUrl.CREATE_USER_URL, data=user)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_value_by_name(
            response, 'success', True, Data.ASSERTIONS_INCORRECT_FILED_ERROR_MESSAGE)

        helper = Helper()
        helper.delete_user(user)

    @allure.title('Создание пользователя. Негативный сценарий. Одно из полей не заполнено. ')
    @allure.description('Создание нового пользователя не происходит, т.к. не заполнено одно из обязательных полей. '
                        'Проверяется корректность кода ответа и сообщения об ошибке')
    @pytest.mark.parametrize("condition",
                             [("no_email"),
                              ("no_password"),
                              ("no_name")])
    def test_create_user_mandatory_field_missed(self, user, condition):
        helper = Helper()
        helper.exclude_parameter(user, condition)

        response = requests.post(ApiUrl.CREATE_USER_URL, data=user)
        Assertions.assert_code_status(response, 403)
        Assertions.assert_json_value_by_name(
            response,
            'message',
            Data.MANDATORY_FIELDS_ERROR_MESSAGE,
            Data.ASSERTIONS_ERROR_MESSAGE)

    @allure.title('Создание пользователя. Негативный сценарий. Попытка повторного создания существующего клиента. ')
    @allure.description('Создание нового пользователя не происходит, пользователь уже существует. '
                        'Проверяется корректность кода ответа и сообщения об ошибке')
    def test_create_user_already_exist(self, registered_user):
        response = requests.post(ApiUrl.CREATE_USER_URL, data=registered_user)

        Assertions.assert_code_status(response, 403)
        Assertions.assert_json_value_by_name(
            response,
            'message',
            Data.DUPLICATED_USER_ERROR_MESSAGE,
            Data.ASSERTIONS_ERROR_MESSAGE)

