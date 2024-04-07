import allure
import requests

from api_url import ApiUrl
from helpful_classes.assertions import Assertions
from helpful_classes.helper import Helper
from helpful_classes.order_generator import OrderGenerator
from helpful_classes.user_generator import UserGenerator


@allure.epic("Создание заказа")
class TestCreateOrder:

    @allure.title('Создание заказа авторизованным пользователем. Позитивный сценарий')
    @allure.description('Существующий пользователь авторизуется в системе и создает заказ. '
                        'Проверяется корректность кода ответа и сообщения об успехе')
    def test_create_new_order_with_ingredients_by_authorized_user_success(self):
        user = UserGenerator.register_new_user_and_return_login_password()
        order = OrderGenerator.generate_new_order()

        token = Helper.login_as_user(user)
        headers = {"Authorization": token}

        response = requests.post(ApiUrl.CREATE_ORDER_URL, headers=headers, data=order)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_value_by_name(
            response, 'success', True, 'Success field has incorrect value')

        Helper.delete_user(user)

    @allure.title('Создание заказа без авторизации в системе. ')
    @allure.description('Без авторизации в системе создается запрос на создание заказа. '
                        'Проверяется корректность кода ответа и сообщения')
    def test_create_new_order_with_ingredients_without_authorization_success(self):
        order = OrderGenerator.generate_new_order()

        response = requests.post(ApiUrl.CREATE_ORDER_URL,  data=order)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_value_by_name(
            response, 'success', True, 'Success field has incorrect value')

    @allure.title('Создание заказа без ингредиентов. Негативный сценарий')
    @allure.description('Без авторизации в системе создается запрос на создание заказа без ингредиентов. '
                        'Проверяется корректность кода ответа и сообщения об ошибке')
    def test_create_new_order_without_ingredients(self):
        response = requests.post(ApiUrl.CREATE_ORDER_URL)
        Assertions.assert_code_status(response, 400)
        Assertions.assert_json_value_by_name(
            response,
            'message',
            'Ingredient ids must be provided',
            'Error message is incorrect')

    @allure.title('Создание заказа с несуществующим ингредиентом. Негативный сценарий')
    @allure.description('Без авторизации в системе создается запрос на создание заказа с несуществующим ингредиентом. '
                        'Проверяется корректность кода ответа и сообщения об ошибке')
    def test_create_new_order_without_ingredients(self):
        order = OrderGenerator.generate_new_order_non_existing_ingredients()
        response = requests.post(ApiUrl.CREATE_ORDER_URL,  data=order)
        Assertions.assert_code_status(response, 500)









