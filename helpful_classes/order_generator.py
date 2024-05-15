import random

import allure
import requests

from api_url import ApiUrl
from helpful_classes.helper import Helper


class OrderGenerator:

    @allure.step('Генерируется новый заказ')
    def generate_new_order(self):
        response = requests.get(ApiUrl.INGREDIENT_INFO_URL)
        ingredients_dict = response.json()

        ingredients_data = ingredients_dict['data']
        ingredients_count = len(ingredients_data)
        ingredients_list = []
        for i in range (0, 3):
            ingredient_index = random.randint(0, ingredients_count-1)
            ingredient = ingredients_data[ingredient_index]
            ingredient_id = ingredient.get('_id')
            ingredients_list.append(ingredient_id)

        order_ingredients = {"ingredients": ingredients_list}
        return order_ingredients

    @staticmethod
    @allure.step('Генерируется новый заказ с несуществующими ингредиентами')
    def generate_new_order_non_existing_ingredients():
        ingredients_list = []
        helper = Helper()
        ingredient_1 = f'1234{helper.generate_random_string(20)}'
        ingredient_2 = f'2123{helper.generate_random_string(20)}'

        ingredients_list.append(ingredient_1)
        ingredients_list.append(ingredient_2)
        order_ingredients = {"ingredients": ingredients_list}
        return order_ingredients

