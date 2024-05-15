import pytest

from helpful_classes.helper import Helper
from helpful_classes.order_generator import OrderGenerator
from helpful_classes.user_generator import UserGenerator


@pytest.fixture(scope='function')
def user():
    user_generator = UserGenerator()
    user = user_generator.create_new_user_and_return_login_password()
    return user


@pytest.fixture(scope='function')
def registered_user():
    user_generator = UserGenerator()
    r_user = user_generator.register_new_user_and_return_login_password()
    yield r_user
    helper = Helper()
    helper.delete_user(r_user)


@pytest.fixture(scope='function')
def order():
    order_generator = OrderGenerator()
    order = order_generator.generate_new_order()
    return order


