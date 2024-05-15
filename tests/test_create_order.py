import allure
import requests

from api_url import ApiUrl
from data import Data
from helpful_classes.assertions import Assertions
from helpful_classes.helper import Helper


@allure.epic("Создание заказа")
class TestCreateOrder:

    @allure.title('Создание заказа авторизованным пользователем. Позитивный сценарий')
    @allure.description('Существующий пользователь авторизуется в системе и создает заказ. '
                        'Проверяется корректность кода ответа и сообщения об успехе')
    def test_create_new_order_with_ingredients_by_authorized_user_success(self, registered_user, order):
        helper = Helper()
        token = helper.login_as_user(registered_user)
        headers = {"Authorization": token}

        response = requests.post(ApiUrl.CREATE_ORDER_URL, headers=headers, data=order)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_value_by_name(
            response, 'success', True, Data.ASSERTIONS_INCORRECT_FILED_ERROR_MESSAGE)

    @allure.title('Создание заказа без авторизации в системе. ')
    @allure.description('Без авторизации в системе создается запрос на создание заказа. '
                        'Проверяется корректность кода ответа и сообщения')
    def test_create_new_order_with_ingredients_without_authorization_success(self, order):
        response = requests.post(ApiUrl.CREATE_ORDER_URL,  data=order)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_value_by_name(
            response, 'success', True, Data.ASSERTIONS_INCORRECT_FILED_ERROR_MESSAGE)

    @allure.title('Создание заказа без ингредиентов. Негативный сценарий')
    @allure.description('Без авторизации в системе создается запрос на создание заказа без ингредиентов. '
                        'Проверяется корректность кода ответа и сообщения об ошибке')
    def test_create_new_order_without_ingredients(self):
        response = requests.post(ApiUrl.CREATE_ORDER_URL)
        Assertions.assert_code_status(response, 400)
        Assertions.assert_json_value_by_name(
            response,
            'message',
            Data.TCO_NO_INGREDIENTS_ERROR_MESSAGE,
            Data.ASSERTIONS_ERROR_MESSAGE)

    @allure.title('Создание заказа с несуществующим ингредиентом. Негативный сценарий')
    @allure.description('Без авторизации в системе создается запрос на создание заказа с несуществующим ингредиентом. '
                        'Проверяется корректность кода ответа и сообщения об ошибке')
    def test_create_new_order_with_non_existing_ingredients(self, order):
        response = requests.post(ApiUrl.CREATE_ORDER_URL,  data=order)
        Assertions.assert_code_status(response, 200)









