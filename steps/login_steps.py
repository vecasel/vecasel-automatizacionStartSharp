from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_login import LoginPage


# Given steps
@given(u'I am on the Serenity Demo login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://serenity.is/demo/")


# When steps
@when(u'I enter my username as "{username}" and my password as "{password}"')
def step_impl(context, username, password):
    login_page = LoginPage(context.driver)
    login_page.enter_username(username)
    login_page.enter_password(password)


@when(u'I click the sign in button')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_sign_in_button()


# Then steps
@then(u'I should be redirected to the dashboard page')
def step_impl(context):
    dashboard_title = WebDriverWait(context.driver, 10).until(EC.title_is("Dashboard - StartSharp"))
    assert dashboard_title


@then(u'the page title should be "{expected_title}"')
def step_impl(context, expected_title):
    actual_title = context.driver.title
    assert actual_title == expected_title


@then(u'I should see the text "{expected_text}" in the h1 element')
def step_impl(context, expected_text):
    h1_element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    actual_text = h1_element.text
    assert actual_text == expected_text
