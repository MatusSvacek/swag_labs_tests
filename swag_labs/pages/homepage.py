from pylenium.driver import Pylenium

from swag_labs.pages.pagebase import PageBase


class HomePage(PageBase):
    def __init__(self, py: Pylenium):
        super().__init__(py)
        self.py = py

    # Locators

    ADD_TO_CART_BUTTON = ".btn_primary"
    ITEM_TITLE = ".inventory_item_name"
    ITEMS = ".inventory_item"
    REMOVE_BUTTON = ".btn_secondary"
    SHOPPING_CART_BADGE = ".shopping_cart_badge"
    FILTER_BUTTON = ".select_container"
    SORT_BUTTON_ZA = "//option[@value='za']"

    def add_item_to_cart(self, item_desc: str):
        products = self.py.find(self.ITEMS)
        for product in products:
            item_name = product.get(self.ITEM_TITLE).text()
            if item_name == item_desc:
                product.get(self.ADD_TO_CART_BUTTON).should().be_clickable().click()
                break

    def remove_item_from_cart(self, item_desc: str):
        products = self.py.find(self.ITEMS)
        for product in products:
            item_name = product.get(self.ITEM_TITLE).text()
            if item_name == item_desc:
                product.get(self.REMOVE_BUTTON).should().be_clickable().click()
                break

    def click_filter_button(self):
        self.py.get(self.FILTER_BUTTON).should().be_clickable().click()

    def click_sort_za(self):
        self.py.getx(self.SORT_BUTTON_ZA).should().be_visible().click()

    def get_all_product_titles(self):
        titles_list = []
        fragrances = self.py.find(self.ITEM_TITLE)
        for fragrance in fragrances:
            titles_list.append(fragrance.text())
        return titles_list
