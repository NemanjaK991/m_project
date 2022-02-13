from selenium.webdriver.common.by import By


class CommonLocators:
    notification_success = (By.CSS_SELECTOR, '.bar-notification.success .content')
    close_notification = (By.CSS_SELECTOR, '#bar-notification .close')
    shopping_cart_header_icon = (By.CSS_SELECTOR, '#topcartlink a span')
    search_input_field = (By.CSS_SELECTOR, '#small-search-box-form input')
    search_button = (By.CSS_SELECTOR, '#small-search-box-form button')


class ShoppingCartLocators:
    empty_cart_message = (By.CSS_SELECTOR, '.order-summary-content .no-data')


class ItemPageLocators:
    no_data_mss = (By.CSS_SELECTOR, '.no-result')