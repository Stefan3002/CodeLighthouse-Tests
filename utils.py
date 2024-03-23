import time
import unittest

from selenium.webdriver.common.by import By

error_msgs = {
    "log_in": {
        "user_not_found": "AppUser matching query does not exist.",
        "wrong_password": "Wrong credentials!",
        'provider': 'It appears this is a provider account! Maybe try Google or Github from down below?'
    }
}
login_credentials = {
    "username": "secrieru23022@gmail.com",
    "password": "4d528af3a21b497e996d1dfcb50366ec",
    "provider_username": "stefan.secrieru02@e-uvt.ro"
}



def wait_for_page_transition():
    time.sleep(3)

def wait_for_paint(time_s):
    time.sleep(time_s)

def hide_runtime_error(driver):
    runtime_error = driver.find_elements(By.ID, 'webpack-dev-server-client-overlay')
    if len(runtime_error):
        driver.execute_script("arguments[0].style.display = 'none';", runtime_error[0])



class Utils(unittest.TestCase):
    def correct_log_in(self, driver):
        driver.get('http://localhost:3000/auth')

        wait_for_page_transition()

        hide_runtime_error(driver)

        username = driver.find_elements(By.ID, 'log-in-username')
        self.assertEqual(len(username), 1, "Can't find the log-in username field!")

        password = driver.find_elements(By.ID, 'log-in-password')
        self.assertEqual(len(password), 1, "Can't find the log-in password field!")

        log_in_button = driver.find_elements(By.ID, 'log-in-button')
        self.assertEqual(len(log_in_button), 1, "Can't find the log-in button!")

        password[0].send_keys(login_credentials['password'])
        username[0].send_keys(login_credentials['username'])

        log_in_button[0].click()

        wait_for_page_transition()

        error_msg = driver.find_elements(By.ID, 'error-message')

        self.assertEqual(len(error_msg), 0, "There was an error!")

        parallax = driver.find_elements(By.CLASS_NAME, 'parallax')
        self.assertEqual(len(parallax), 1, "The home page was not displayed!")