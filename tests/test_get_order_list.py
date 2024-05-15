import allure
import requests

from api_url import ApiUrl
from data import Data
from helpful_classes.assertions import Assertions
from helpful_classes.helper import Helper


@allure.epic("Получение списка заказов")
class TestGetOrderList:

    @allure.title('Получение данных о заказах авторизованного пользователя. Позитивный сценарий')
    @allure.description('Существующий пользователь авторизуется в системе и запрашивает список своих заказов. '
                        'Проверяется корректность кода ответа и сообщения об успехе')
    def test_get_order_list_by_autorized_user(self, registered_user):
        helper = Helper()
        token = helper.login_as_user(registered_user)
        headers = {"Authorization": token}

        response = requests.get(ApiUrl.GET_USERS_ORDERS, headers=headers)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, 'orders')

    @allure.title('Запрос данных о заказах без авторизации. Негативный сценарийю')
    @allure.description('Системе отправляется запрос на получение списока заказов без авторизации в системе. '
                        'Проверяется корректность кода ответа и сообщения об ошибке')
    def test_get_order_list_without_authorization(self):
        response = requests.get(ApiUrl.GET_USERS_ORDERS)
        Assertions.assert_code_status(response, 401)
        Assertions.assert_json_value_by_name(
            response,
            'message',
            Data.NOT_AUTHORIZED_ERROR_MESSAGE,
            Data.ASSERTIONS_ERROR_MESSAGE)
