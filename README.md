#Stellar Burgers

## test_create_user
Создание пользователя:
 - создать уникального пользователя;
 - создать пользователя, который уже зарегистрирован;
 - создать пользователя и не заполнить одно из обязательных полей.

## test_login
Логин пользователя:
 - логин под существующим пользователем,
 - логин с неверным логином и паролем.

## test_user_data_update
Изменение данных пользователя:
 - с авторизацией,
 - без авторизации,
 - возможность изменения каждого из полей

## test_create_order
Создание заказа:
 - с авторизацией,
 - без авторизации,
 - с ингредиентами,
 - без ингредиентов,
 - с неверным хешем ингредиентов.

## test_get_order_list
Получение заказов конкретного пользователя:
 - авторизованный пользователь,
 - неавторизованный пользователь.

## Запуск тестов и формирование отчета allure
запустить все тесты в директории tests/
python -m pytest tests/

сгенерировать отчет
pytest tests/ --alluredir=allure_results

сформировать отчёт в формате веб-страницы
allure serve allure_results