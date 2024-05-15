class ApiUrl:

    BASE_API_URL = 'https://stellarburgers.nomoreparties.site/api/'

    # API для создания нового пользователя POST https://stellarburgers.nomoreparties.site/api/auth/register
    CREATE_USER_URL = f'{BASE_API_URL}auth/register'
    # API для создания нового заказа POST https://stellarburgers.nomoreparties.site/api/orders
    CREATE_ORDER_URL = f'{BASE_API_URL}orders'
    # API для получения информации об ингредиентах GET https://stellarburgers.nomoreparties.site/api/ingredients
    INGREDIENT_INFO_URL = f'{BASE_API_URL}ingredients'
    # API для aвторизации пользователя POST https://stellarburgers.nomoreparties.site/api/auth/login
    AUTH_USER_URL = f'{BASE_API_URL}auth/login'
    # API для олучения заказов конкретного пользователя GET https://stellarburgers.nomoreparties.site/api/orders
    GET_USERS_ORDERS = f'{BASE_API_URL}orders'

    # API для удаления пользователя DELETE https://stellarburgers.nomoreparties.site/api/auth/user
    # !!! ссылка дается полностью, т.к. при замене на f- строку с BASE_API_URL запросы не отрабатывают !!!
    DELETE_USER_URL = "https://stellarburgers.nomoreparties.site/api/auth/user"

    # API для обновления данных пользователя PATCH "https://stellarburgers.nomoreparties.site/api/auth/user"
    # !!! ссылка дается полностью, т.к. при замене на f- строку с BASE_API_URL запросы не отрабатывают !!!
    UPDATE_USER_DATA_URL = "https://stellarburgers.nomoreparties.site/api/auth/user"

