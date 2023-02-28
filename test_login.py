import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.NAME, "Username")
        self.password = (By.NAME, "Password")
        self.submit_button = (By.TAG_NAME, "button")

    def enter_username(self, username_text):
        username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username))
        username.clear()
        username.send_keys(username_text)

    def enter_password(self, password_text):
        password = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password))
        password.clear()
        password.send_keys(password_text)

    def click_sign_in_button(self):
        submit_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.submit_button))
        submit_button.click()


class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://serenity.is/demo/")
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_with_valid_credentials(self):
        self.login_page.enter_username("admin")
        self.login_page.enter_password("serenity")
        self.login_page.click_sign_in_button()
        dashboard_title = WebDriverWait(self.driver, 10).until(EC.title_is("Dashboard - StartSharp"))
        dashboard_h1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.assertTrue(dashboard_title)
        self.assertEqual(dashboard_h1.text, "Dashboard")
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
