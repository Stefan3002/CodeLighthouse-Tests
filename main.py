import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

from utils import wait_for_page_transition, hide_runtime_error, wait_for_paint, error_msgs, login_credentials, \
    Utils



class HomePgeTest(unittest.TestCase):
    def setUp(self):
        # The webdriver is a component that controls the browser
        service = Service(executable_path="msedgedriver.exe")
        self.driver = webdriver.Edge(service=service)
        self.driver.get('http://localhost:3000/')
        Utils.correct_log_in(self, self.driver)

    def test_community_copy_to_clipboard(self):
        # wait_for_page_transition()
        copy_clipboard = self.driver.find_elements(By.CLASS_NAME, 'copy-to-clipboard')
        self.assertEqual(len(copy_clipboard), 1, "No community with a copy to clipboard button found!")

        community_code = self.driver.find_elements(By.CLASS_NAME, 'community-enrollment_code')

        self.assertEqual(len(community_code), 1, 'There was no community code displayed anywhere!')

        copy_clipboard[0].click()

        wait_for_paint(1)

        pop_up = self.driver.find_elements(By.ID, 'pop-up-data')
        self.assertEqual(len(pop_up), 1, "There was no pop-up displayed!")

        # self.assertEqual(clipboard_content, community_code[0].text, 'The code was not copied correctly')

    def tearDown(self):
        self.driver.quit()

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

    def test_wrong_credentials_username(self):
        self.driver.get('http://localhost:3000/auth')

        wait_for_page_transition()

        hide_runtime_error(self.driver)

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

    def test_wrong_credentials_password(self):
        self.driver.get('http://localhost:3000/auth')

        wait_for_page_transition()

        hide_runtime_error(self.driver)

        username = self.driver.find_elements(By.ID, 'log-in-username')
        self.assertEqual(len(username), 1, "Can't find the log-in username field!")

        password = self.driver.find_elements(By.ID, 'log-in-password')
        self.assertEqual(len(password), 1, "Can't find the log-in password field!")

        log_in_button = self.driver.find_elements(By.ID, 'log-in-button')
        self.assertEqual(len(log_in_button), 1, "Can't find the log-in button!")

        password[0].send_keys('invalid_password')
        username[0].send_keys(login_credentials['username'])

        log_in_button[0].click()

        wait_for_paint(2)

        error_msg = self.driver.find_elements(By.ID, 'error-message')

        self.assertEqual(len(error_msg), 1, "Error was not displayed after using invalid password!")
        self.assertEqual(error_msg[0].text, error_msgs['log_in']['wrong_password'], "Error text does not match the expected one!")

    def test_correct_credentials(self):
        Utils.correct_log_in(self, self.driver)

    def test_wrong_credentials_provider(self):
        self.driver.get('http://localhost:3000/auth')

        wait_for_page_transition()

        hide_runtime_error(self.driver)

        username = self.driver.find_elements(By.ID, 'log-in-username')
        self.assertEqual(len(username), 1, "Can't find the log-in username field!")

        password = self.driver.find_elements(By.ID, 'log-in-password')
        self.assertEqual(len(password), 1, "Can't find the log-in password field!")

        log_in_button = self.driver.find_elements(By.ID, 'log-in-button')
        self.assertEqual(len(log_in_button), 1, "Can't find the log-in button!")

        username[0].send_keys(login_credentials['provider_username'])

        log_in_button[0].click()

        wait_for_paint(2)

        error_msg = self.driver.find_elements(By.ID, 'error-message')

        self.assertEqual(len(error_msg), 1, "Error was not displayed after using provider e-mail!")
        self.assertEqual(error_msg[0].text, error_msgs['log_in']['provider'],
                         "Error text does not match the expected one!")


    def tearDown(self):
            self.driver.quit()
