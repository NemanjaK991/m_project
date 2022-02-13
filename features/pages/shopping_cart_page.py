from features.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from features.pages.locators import ShoppingCartLocators


class ShoppingCartPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.empty_cart_message = ShoppingCartLocators.empty_cart_message

    def return_all_added_products(self):
        products = (By.CSS_SELECTOR, 'tbody tr .product-name')
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(products)
        )
        all_added_products = []
        for product in self.driver.find_elements(*products):
            all_added_products.append(product.text)
        return all_added_products

    def return_quantity_value_for_first_product(self):
        product = (By.CSS_SELECTOR, 'tbody tr .quantity input[class="qty-input"]')
        return self.get_text_from_input_field(product)

    def remove_nth_product(self, product_number):
        remove_btn = (By.CSS_SELECTOR, 'tbody tr:nth-child({}) .remove-from-cart button'.format(product_number))
        self.click_on_element(remove_btn)

    def return_empty_cart_message(self):
        return self.return_text_from_element(self.empty_cart_message)


