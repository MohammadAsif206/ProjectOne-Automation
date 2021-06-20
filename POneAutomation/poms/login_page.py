from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement


class Login:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def username_bar(self):
        element: WebElement = self.driver.find_element_by_id("userId")
        return element

    def password_bar(self):
        element: WebElement = self.driver.find_element_by_id("userPassword")
        return element

    def signin_button(self):
        element: WebElement = self.driver.find_element_by_id("submitBtn")
        return element
