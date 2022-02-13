from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from features.pages.locators import CommonLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, element):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(element))
        self.driver.find_element(*element).click()

    def return_text_from_element(self, element):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(element))
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(element))
        return self.driver.find_element(*element).text

    def input_values(self, element, value):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(element)
        )
        self.driver.find_element(*element).clear()
        self.driver.find_element(*element).send_keys(value)

    def get_text_from_input_field(self, element):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(element)
        )
        return self.driver.find_element(*element).get_attribute('value')

    def select_nth_dropdown_option_from_nth_top_menu_option(self, top_menu_option, dropdown_option):
        top_menu_option_selector = (By.XPATH, "//div[contains(@class, 'header-menu')]/ul/li[{}]".format(top_menu_option))
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(top_menu_option_selector)
        )
        top_menu_option_element = self.driver.find_element(*top_menu_option_selector)
        hover = ActionChains(self.driver).move_to_element(top_menu_option_element)
        hover.perform()
        dropdown_option_selector = (By.XPATH,
                                    "//div[contains(@class, 'header-menu')]/ul/li[{}]/"
                                    "ul[contains(@class, 'sublist first-level')]/li[{}]".format(
                                        top_menu_option, dropdown_option))
        self.click_on_element(dropdown_option_selector)

    def return_success_notification_msg(self):
        return self.return_text_from_element(CommonLocators.notification_success)

    def click_on_close_notification_button(self):
        self.click_on_element(CommonLocators.close_notification)
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located(CommonLocators.close_notification)
        )

    def scroll_element_into_view(self, element_selector):
        el = self.driver.find_element(*element_selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", el)

    def click_on_shopping_cart_header_icon(self):
        self.click_on_element(CommonLocators.shopping_cart_header_icon)



