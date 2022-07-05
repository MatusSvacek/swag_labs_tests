from pylenium.driver import Pylenium

from swag_labs.pages.pagebase import PageBase


class LoginPage(PageBase):
    def __init__(self, py: Pylenium):
        super().__init__(py)
        self.py = py

    # Locators

    USER_NAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
