from pylenium.driver import Pylenium

from swag_labs.pages.cart_page import CartPage
from swag_labs.pages.homepage import HomePage
from swag_labs.pages.login_page import LoginPage
from swag_labs.pages.navigation import Navigation


class SwagPages:
    def __init__(self, py: Pylenium):
        self.py = py
        self.navigation = Navigation(py)
        self.homepage = HomePage(py)
        self.login_page = LoginPage(py)
        self.cart_page = CartPage(py)
