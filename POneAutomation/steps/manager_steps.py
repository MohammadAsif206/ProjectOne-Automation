from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.alert import Alert
import time

#
# @given('The Guest is on the manager Page')
# def manager_page(context):
#     context.driver.get('file:///C:/Users/moham/PycharmProjects/ProjectOne/frontend/manager.html')
#     context.driver.implicitly_wait(10)
#     time.sleep(2)


@when('The Guest types {id} into the id bar')
def step_impl(context, id: int):
    context.manager.id_bar().send_keys(id)


@when('The Guest types {status} into the request status bar')
def step_impl(context, status: str):
    context.manager.status_bar().send_keys(status)


@when('The Guest types {comment} into the request comment bar')
def step_impl(context, comment: str):
    context.manager.comment_bar().send_keys(comment)


@when('The Guest clicks on the request submit button')
def step_impl(context):
    time.sleep(2)
    context.manager.submit_button().click()
    time.sleep(2)
