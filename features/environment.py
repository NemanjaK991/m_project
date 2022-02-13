import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), r'..'))
from selenium import webdriver
from features import configuration
import allure
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

link = configuration.link
browser = configuration.browser


def before_all(context):

    if configuration.automatic_download_driver:
        if browser == 'Chrome':
            context.selenium_driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browser == 'Firefox':
            context.selenium_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser == 'Edge':
            context.selenium_driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    else:
        if browser == 'Chrome':
            context.selenium_driver = webdriver.Chrome(executable_path=configuration.chrome_driver_path)
        elif browser == 'Firefox':
            context.selenium_driver = webdriver.Firefox(executable_path=configuration.firefox_driver_path)

        elif browser == 'Edge':
            context.selenium_driver = webdriver.Edge(executable_path=configuration.edge_driver_path)
    context.link = link
    context.selenium_driver.maximize_window()


def after_scenario(context, scenario):

    if scenario.status == 'failed':
        allure.attach(context.selenium_driver.get_screenshot_as_png(), f"{scenario.name} - FAILED",
                      allure.attachment_type.PNG)

    context.selenium_driver.execute_script("window.localStorage.clear();")
    context.selenium_driver.execute_script("window.sessionStorage.clear();")
    context.selenium_driver.delete_all_cookies()
    context.selenium_driver.refresh()


def after_all(context):
    context.selenium_driver.quit()