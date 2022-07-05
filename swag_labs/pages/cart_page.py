from pylenium.driver import Pylenium

from settings import FIRST_NAME, LAST_NAME, ZIP_CODE


class CartPage:
    def __init__(self, py: Pylenium):
        self.py = py

    # Locators

    CART_LIST = ".cart_list"
    ITEM_TITLE = ".inventory_item_name"
    CHECKOUT_BUTTON = "#checkout"
    TITLE = ".title"

    # Checkout

    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    ZIP_CODE_INPUT = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    CANCEL_BUTTON = "#cancel"

    # Finish

    FINISH_BUTTON = "#finish"

    def get_cart_list(self):
        return self.py.get(self.CART_LIST)

    def click_on_checkout(self):
        self.py.get(self.CHECKOUT_BUTTON).should().be_clickable().click()

    def get_title_text(self):
        return self.py.get(self.TITLE).text()

    # Checkout information

    def fill_checkout_info(self):
        self.py.get(self.FIRST_NAME_INPUT).should().be_visible().type(FIRST_NAME)
        self.py.get(self.LAST_NAME_INPUT).should().be_visible().type(LAST_NAME)
        self.py.get(self.ZIP_CODE_INPUT).should().be_visible().type(ZIP_CODE)

    def click_continue_checkout_button(self):
        self.py.get(self.CONTINUE_BUTTON).should().be_clickable().click()

    def click_cancel_checkout_button(self):
        self.py.get(self.CANCEL_BUTTON).should().be_clickable().click()

    def click_finish_button(self):
        self.py.get(self.FINISH_BUTTON).should().be_clickable().click()
