def test_add_item_to_cart(swag, login):
    swag.homepage.add_item_to_cart("Sauce Labs Bike Light")

    assert swag.py.get(swag.homepage.SHOPPING_CART_BADGE).should().be_visible()


def test_remove_product_from_cart(swag, login):
    swag.homepage.add_item_to_cart("Sauce Labs Fleece Jacket")
    swag.homepage.remove_item_from_cart("Sauce Labs Fleece Jacket")

    assert swag.py.should().not_find(swag.homepage.SHOPPING_CART_BADGE)


def test_sort_products_za(swag, login):
    titles_before_sort = swag.homepage.get_all_product_titles()
    swag.homepage.click_filter_button()
    swag.homepage.click_sort_za()
    titles_after_sort = swag.homepage.get_all_product_titles()

    assert sorted(titles_before_sort, key=str.lower, reverse=True) == titles_after_sort


def test_cart_items_counter(swag, login):
    swag.homepage.add_item_to_cart("Sauce Labs Bike Light")
    swag.homepage.add_item_to_cart("Sauce Labs Fleece Jacket")

    assert swag.py.get(swag.homepage.SHOPPING_CART_BADGE).text() == "2"





