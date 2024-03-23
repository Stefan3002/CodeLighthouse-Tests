import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

error_msgs = {
    "log_in": {
        "user_not_found": "AppUser matching query does not exist."
    }
}

def wait_for_page_transition():
    time.sleep(3)

def wait_for_paint(time_s):
    time.sleep(time_s)

class LogInTestViaCredentials(unittest.TestCase):
    def setUp(self):
        # The webdriver is a component that controls the browser
        service = Service(executable_path="msedgedriver.exe")
        self.driver = webdriver.Edge(service=service)
        self.driver.get('http://localhost:3000/')

    def test_navigation_to_login(self):
        log_in_anchor = self.driver.find_elements(By.ID, 'log-in-anchor')
        self.assertEqual(len(log_in_anchor), 1, "Can't find the log-in anchor on the home page!")
        log_in_anchor[0].click()

        wait_for_page_transition()

        log_in_button = self.driver.find_elements(By.ID, 'log-in-button')
        self.assertEqual(len(log_in_button), 1, "Can't find the log-in via credentials button!")

    def test_wrong_credentials(self):
        self.driver.get('http://localhost:3000/auth')

        wait_for_page_transition()

        runtime_error = self.driver.find_elements(By.ID, 'webpack-dev-server-client-overlay')
        if len(runtime_error):
            self.driver.execute_script("arguments[0].style.display = 'none';", runtime_error[0])

        username = self.driver.find_elements(By.ID, 'log-in-username')
        self.assertEqual(len(username), 1, "Can't find the log-in username field!")

        password = self.driver.find_elements(By.ID, 'log-in-password')
        self.assertEqual(len(password), 1, "Can't find the log-in password field!")

        log_in_button = self.driver.find_elements(By.ID, 'log-in-button')
        self.assertEqual(len(log_in_button), 1, "Can't find the log-in button!")

        username[0].send_keys('invalid_username')

        log_in_button[0].click()

        wait_for_paint(2)

        error_msg = self.driver.find_elements(By.ID, 'error-message')

        self.assertEqual(len(error_msg), 1, "Error was not displayed after using invalid username!")
        self.assertEqual(error_msg[0].text, error_msgs['log_in']['user_not_found'], "Error text does not match the expected one!")


    def tearDown(self):
        self.driver.quit()
