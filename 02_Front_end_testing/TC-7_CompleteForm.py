import time
import requests
from faker import Faker
import unittest
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# import HtmlTestRunner

# ...............Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# ..............Set path to chromedriver as per your configuration
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
# ................................................................
fake = Faker()


def delay():
    time.sleep(random.randint(1, 3))  # Delay all actions from 1 to 3 sec

    # # .............Cross browser.............................................
    # # from webdriver_manager.firefox import GeckoDriverManager
    # # from webdriver_manager.microsoft import EdgeChromiumDriverManager
    # # from selenium.webdriver.firefox.service import Service
    # # from selenium.webdriver.edge.service import Service


# ...........ChromeBrowser:........................................


class ChromeBrowser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    # ......Verify the webpage is accessible.........................
    # ......(Methods in UnitTest should start from "test" keyword).......
    def test0_webpage_search(self):
        driver1 = self.driver

        # .........Check that an element is present on the DOM of a page and visible.
        url = "https://api.nasa.gov/"
        driver1.get(url)
        driver1.maximize_window()
        driver1.minimize_window()
        driver1.maximize_window()

        # ................API testing from Selenium....................
        print("Webpage Url has", requests.get(url).status_code, "as status Code")
        code = requests.get(url).status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200", "Current code is:", code)

        # .................Check current webpage Title with Exception functionality
        try:
            assert "NASA Open APIs" in driver1.title
            print("Webpage is CORRECT. Current Title is: ", driver1.title)
        except WDE:
            print("Webpage is different, current Title is: ", driver1.title)

        # Delay all actions from 1 to 3 sec
        delay()

    def tearDown(self):
        self.driver.quit()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ...............  NP-T7: "Verify The system generates an API key..."  ......

    def test7_complete_form_search(self):
        driver7 = self.driver
        url = "https://api.nasa.gov/"
        driver7.get(url)
        driver7.maximize_window()
        delay()
        try:
            # ...... FIRST NAME. Execute JavaScript to access shadow DOM and get the field .....
            FName = fake.first_name()

            element = driver7.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector("#user_first_name")').send_keys(FName)
            print("First Name: ", FName)
            # # ....... Now you can interact with the element ......
            # # ....... For example, to input text:
            # element.send_keys('Your text here')
        except NoSuchElementException:
            print("FIRST NAME field NOT DISPLAYED")

        try:
            # ....... LAST NAME. Execute JavaScript to access shadow DOM and get the field .....

            LName = fake.last_name()

            element = driver7.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector("#user_last_name")').send_keys(LName)
            print("Last Name: ", LName)  # For the records.

        except NoSuchElementException:
            print("LAST NAME field NOT DISPLAYED")

        try:
            # ....... EMAIL. Execute JavaScript to access shadow DOM and get the field .....
            email = fake.email()

            element = driver7.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector("#user_email")').send_keys(email)
            print(email)  # For the records.

        except NoSuchElementException:
            print("EMAIL field NOT DISPLAYED")

        try:
            # ...... SIGNUP button. Execute JavaScript to access shadow DOM and get the element ...
            element = driver7.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector(".btn.btn-lg.btn-primary")').click()

        except NoSuchElementException:
            print("SIGNUP button NOT DISPLAYED")


delay()


def tearDown(self):
    self.driver.quit()
