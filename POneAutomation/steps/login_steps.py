from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.alert import Alert
import time


@given('The Guest is on the login Home Page')
def open_signin_page(context):
    context.driver.get('file:///C:/Users/moham/PycharmProjects/ProjectOne/frontend/sign_in.html')
    context.driver.implicitly_wait(10)
    time.sleep(2)


@when('The Guest types Mohammad into the username bar')
def step_impl(context):
    context.signin.username_bar().send_keys('Mohammad')


@when('The Guest types Asif into the password bar')
def step_impl(context):
    context.signin.password_bar().send_keys('Asif')
    time.sleep(2)


@when('The Guest clicks on the signin button')
def step_impl(context):
    time.sleep(2)
    context.signin.signin_button().click()
    time.sleep(2)


@when('The guest clicks ok on alert prompt')
def step_impl(context):
    alert = context.driver.switch_to.alert
    alert.accept()
    time.sleep(2)


@then('The guest should be on employee page')
def step_impl(context):
    title = context.driver.title
    assert title == "Employees"
    time.sleep(2)


@then('The alert prompts and say Welcome to employee')
def step_impl(context):
    alert = context.driver.switch_to.alert
    text = alert.text
    print(text)
    assert text == ' Welcome Mohammad'

    time.sleep(2)


@when('The Guest types Olive into the username bar')
def step_impl(context):
    context.signin.username_bar().send_keys('Olive')


@when('The Guest types Oil into the password bar')
def step_impl(context):
    context.signin.password_bar().send_keys('Oil')
    time.sleep(2)


@then('The alert prompts and and say Welcome to manager')
def step_impl(context):
    alert = context.driver.switch_to.alert
    text = alert.text
    print(text)
    assert text == 'Olive  welcome'

    time.sleep(2)


@then('The guest should be on manager page')
def step_impl(context):
    title = context.driver.title
    assert title == "Manager"
    time.sleep(2)


@when('The Guest types Cold into the username bar')
def step_impl(context):
    context.signin.username_bar().send_keys('Cold')


@when('The Guest types Winter into the password bar')
def step_impl(context):
    context.signin.password_bar().send_keys('Winter')


@then('The alert prompts and say Either entered username or password is wrong.')
def step_impl(context):
    alert = context.driver.switch_to.alert
    text = alert.text
    assert text == 'Either entered username or password is wrong.'
    time.sleep(2)
