from selenium import webdriver
from poms.login_page import Login
from  poms.employee_page import Employee
from poms.manager_page import Manager
from selenium.webdriver.chrome.webdriver import WebDriver
from behave.runner import Context


# Environment is like a configuration for you cucumber tests
# it is actual python code

# The context object passed into out step implementation and environment set and tear down functions
# is shared between every function
# context is a singleton (there is one context object for the eniterty of the program)
# context is the primary way to share info for our object in your code
def before_all(context: Context):
    # ideally you attach the web driver for the application to the context object
    context.driver: WebDriver = webdriver.Chrome('C:\\Users\\moham\\OneDrive\\Desktop\\chromedriver.exe')
    context.signin = Login(context.driver)
    context.employee = Employee(context.driver)
    context.manager = Manager(context.driver)

    print("I run before ANY scenarios")


def after_all(context: Context):
    print("I run after ANY scenarios")
    context.driver.quit()
