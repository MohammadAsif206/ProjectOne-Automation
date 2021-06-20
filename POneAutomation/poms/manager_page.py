from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class Manager:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def id_bar(self):
        element: WebElement = self.driver.find_element_by_id("erquestIdInput")
        return element

    def status_bar(self):
        element: WebElement = self.driver.find_element_by_id("rstatusInput")
        return element

    def comment_bar(self):
        element: WebElement = self.driver.find_element_by_id("messageInput")
        return element

    def submit_button(self):
        element: WebElement = self.driver.find_element_by_id("btn")
        return element
