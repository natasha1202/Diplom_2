from copy import deepcopy

import allure
import pytest
import requests

from api_url import ApiUrl
from helpful_classes.assertions import Assertions
from helpful_classes.helper import Helper
from helpful_classes.user_generator import UserGenerator


@allure.epic("Обновление данных пользователя")
class TestUserDataUpdate:

    updated_data=[("email"),
                  ("password"),
                  ("name")
                  ]

    @allure.title('Обновление данных пользователя. Позитивный сценарий')
    @allure.description('Существующий пользователь успешно авторизуется в системе и обновляет свои данные. '
                        'Проверяется корректность кода ответа и сообщения об успехе')
    @pytest.mark.parametrize("condition", updated_data)
    def test_update_user_data_authorized_user(self, condition):
        user = UserGenerator.register_new_user_and_return_login_password()
        token = Helper.login_as_user(user)
        new_data = Helper.update_data(user, condition)

        headers = {"Authorization": token}

        response = requests.patch(ApiUrl.UPDATE_USER_DATA_URL, headers=headers, data=new_data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_value_by_name(
           response, 'success', True, 'Success field has incorrect value')

        Helper.delete_user(user)

    updated_data = [("email"),
                    ("password"),
                    ("name")
                    ]

    @allure.title('Обновление данных пользователя без авторизации. Негативный сценарийю')
    @allure.description('Существующий пользователь без авторизации в системе обновляет свои данные. '
                        'Проверяется корректность кода ответа и сообщения об ошибке')
    @pytest.mark.parametrize("condition", updated_data)
    def test_update_user_data_not_authorized_user(self, condition):
        registered_user = UserGenerator.register_new_user_and_return_login_password()
        user = deepcopy(registered_user)
        new_data = Helper.update_data(registered_user, condition)

        response = requests.patch(ApiUrl.UPDATE_USER_DATA_URL, data=new_data)
        Assertions.assert_code_status(response, 401)
        Assertions.assert_json_value_by_name(
            response,
            'message',
            'You should be authorised',
            'Error message is incorrect')
        Helper.delete_user(user)

