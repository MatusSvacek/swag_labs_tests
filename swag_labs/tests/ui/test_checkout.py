def test_buy_product(swag, login):
    swag.homepage.add_item_to_cart("Sauce Labs Bike Light")
    swag.navigation.go_to_cart()
    swag.cart_page.click_on_checkout()

    assert swag.cart_page.get_title_text() == "CHECKOUT: YOUR INFORMATION"

    swag.cart_page.fill_checkout_info()
    swag.cart_page.click_continue_checkout_button()

    assert swag.cart_page.get_title_text() == "CHECKOUT: OVERVIEW"

    swag.cart_page.click_finish_button()

    assert swag.cart_page.get_title_text() == "CHECKOUT: COMPLETE!"


