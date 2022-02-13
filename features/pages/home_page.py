from features.pages.base_page import BasePage
from features.pages.locators import CommonLocators


class HomePage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.search_input_field = CommonLocators.search_input_field
        self.search_button = CommonLocators.search_button

    def input_search_value(self, value):
        self.input_values(self.search_input_field, value)

    def click_on_search_btn(self):
        self.click_on_element(self.search_button)