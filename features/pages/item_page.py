from features.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from features.pages.locators import ItemPageLocators
from selenium.common.exceptions import TimeoutException


class ItemPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.no_product_msg = ItemPageLocators.no_data_mss

    def add_nth_item_in_cart(self, item_number):
        item_selector = (By.CSS_SELECTOR, '.item-grid .item-box:nth-child({}) .buttons button'.format(item_number))
        self.click_on_element(item_selector)

    def return_nth_item_title(self, item_number):
        item_selector = (By.CSS_SELECTOR, '.item-grid .item-box:nth-child({}) .product-title a'.format(item_number))
        return self.return_text_from_element(item_selector)

    def return_all_product_titles(self):
        item_selector = (By.CSS_SELECTOR, '.item-grid .item-box .product-title a')
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(item_selector)
        )
        all_titles = []
        for title in self.driver.find_elements(*item_selector):
            all_titles.append(title.text)
        return all_titles

    def return_number_of_visible_products(self):
        try:
            products = (By.CSS_SELECTOR, '.item-grid .item-box')
            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(products)
            )
            return len(self.driver.find_elements(*products))
        except TimeoutException:
            return 0

    def return_no_product_msg(self):
        return self.return_text_from_element(self.no_product_msg)