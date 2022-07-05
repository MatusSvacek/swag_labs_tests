from pylenium.driver import Pylenium


class Navigation:
    def __init__(self, py: Pylenium):
        self.py = py

    # Locators

    SHOPPING_CART = ".shopping_cart_link"

    def go_to_cart(self):
        self.py.get(self.SHOPPING_CART).should().be_clickable().click()
