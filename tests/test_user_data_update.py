from copy import deepcopy

import allure
import pytest
import requests

from api_url import ApiUrl
from data import Data
from helpful_classes.assertions import Assertions
from helpful_classes.helper import Helper


@allure.epic("Обновление данных пользователя")
class TestUserDataUpdate:

    @allure.title('Обновление данных пользователя. Позитивный сценарий')
    @allure.description('Существующий пользователь успешно авторизуется в системе и обновляет свои данные. '
                        'Проверяется корректность кода ответа и сообщения об успехе')
    @pytest.mark.parametrize("condition", [("email"),
                                           ("password"),
                                           ("name")])
    def test_update_user_data_authorized_user(self, condition, registered_user):
        helper = Helper()
        token = helper.login_as_user(registered_user)
        new_data = helper.update_data(registered_user, condition)

        headers = {"Authorization": token}

        response = requests.patch(ApiUrl.UPDATE_USER_DATA_URL, headers=headers, data=new_data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_value_by_name(
           response, 'success', True, Data.ASSERTIONS_INCORRECT_FILED_ERROR_MESSAGE)

    @allure.title('Обновление данных пользователя без авторизации. Негативный сценарийю')
    @allure.description('Существующий пользователь без авторизации в системе обновляет свои данные. '
                        'Проверяется корректность кода ответа и сообщения об ошибке')
    @pytest.mark.parametrize("condition", [("email"),
                                           ("password"),
                                           ("name")])
    def test_update_user_data_not_authorized_user(self, condition, registered_user):
        helper = Helper()
        n_user = deepcopy(registered_user)
        new_data = helper.update_data(n_user, condition)

        response = requests.patch(ApiUrl.UPDATE_USER_DATA_URL, data=new_data)
        Assertions.assert_code_status(response, 401)
        Assertions.assert_json_value_by_name(
            response,
            'message',
            Data.NOT_AUTHORIZED_ERROR_MESSAGE,
            Data.ASSERTIONS_ERROR_MESSAGE)

