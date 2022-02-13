from behave import *
from features.pages.home_page import HomePage
from features.pages.item_page import ItemPage
from features.pages.locators import CommonLocators
from features.pages.shopping_cart_page import ShoppingCartPage


@given(u'that a User is opened nopCommerce app and a user is positioned on the home page')
def step_impl(context):
    context.selenium_driver.get(context.link)
    context.home_page = HomePage(context.selenium_driver)
    context.item_page = ItemPage(context.selenium_driver)
    context.shopping_cart = ShoppingCartPage(context.selenium_driver)


@when(u'a user selects Camera & photo option from the Electronics menu')
def step_impl(context):
    context.home_page.select_nth_dropdown_option_from_nth_top_menu_option(2, 2)


@when(u'a user clicks on the Add to cart option on the first item')
def step_impl(context):
    context.item_page.add_nth_item_in_cart(1)
    context.added_item = context.item_page.return_nth_item_title(1)


@then(u'the message that product is added is shown')
def step_impl(context):
    assert 'The product has been added to your shopping cart' == context.item_page.return_success_notification_msg()


@then(u'the product is shown in the Shopping cart')
def step_impl(context):
    context.item_page.click_on_close_notification_button()
    context.item_page.scroll_element_into_view(CommonLocators.shopping_cart_header_icon)
    context.item_page.click_on_shopping_cart_header_icon()
    assert context.added_item in context.shopping_cart.return_all_added_products()


@when(u'a user adds two same items into cart')
def step_impl(context):
    context.item_page.add_nth_item_in_cart(1)
    context.item_page.click_on_close_notification_button()
    context.item_page.add_nth_item_in_cart(1)
    context.item_page.click_on_close_notification_button()


@then(u'the quantity value in the cart for the added product is set to 2')
def step_impl(context):
    context.item_page.scroll_element_into_view(CommonLocators.shopping_cart_header_icon)
    context.item_page.click_on_shopping_cart_header_icon()

    assert "2" == context.shopping_cart.return_quantity_value_for_first_product()


@when(u'user opens the Cart page')
def step_impl(context):
    context.item_page.click_on_close_notification_button()
    context.item_page.click_on_shopping_cart_header_icon()


@when(u'user click on the remove button')
def step_impl(context):
    context.shopping_cart.remove_nth_product(1)


@then(u'the product is deleted and appropriate message is shown')
def step_impl(context):
    assert 'Your Shopping Cart is empty!' == context.shopping_cart.return_empty_cart_message()


@when(u'User inputs value in the search field')
def step_impl(context):
    context.inputted_search_value = 'Htc one'
    context.home_page.input_search_value(context.inputted_search_value)


@when(u'user click on the search field')
def step_impl(context):
    context.home_page.click_on_search_btn()


@then(u'searched products are shown')
def step_impl(context):
    if context.item_page.return_number_of_visible_products() > 0:  # check if there is searched value
        counter = 0
        for title in context.item_page.return_all_product_titles():
            if context.inputted_search_value.upper() in title.upper():
                counter += 1
        assert counter == len(context.item_page.return_all_product_titles())
    else:  # if there is no searched value check "no data" value
        assert context.item_page.return_no_product_msg() == 'No products were found that matched your criteria.'
