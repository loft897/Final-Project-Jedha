import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement   # for autocompletion
from prettytable import PrettyTable

# Get the base URL from an environment variable or a file
BASE_URL = os.environ.get('BASE_URL')
# from keys import BASE_URL

class ScrapDelay(webdriver.Chrome):
    def __init__(self, driver_path=r"D:\Projets\Jedha\Final-Project-Jedha\ChromeDrivers", teardown=False, proxy=None):
        # Initialize the webdriver
        self.driver_path = driver_path
        self.teardown = teardown
        self.proxy = proxy
        os.environ['PATH'] += ';' + self.driver_path
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # Add the headless option to run Chrome in the background
        chrome_options.add_argument("--headless")

        if self.proxy is not None:
            chrome_options.add_argument('--proxy-server={}'.format(self.proxy))

        super().__init__(options=chrome_options)
        self.implicitly_wait(5)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close the webdriver if teardown is True
        if self.teardown:
            self.quit()

    def land_first_page(self):
        # Load the first page
        self.get(BASE_URL)

    def cookies(self):
        # Accept the website's cookies
        try:
            cook_choice = self.find_element(
                By.ID, 'onetrust-close-btn-container')

            cook_choice.click()
        except:
            pass

    def select_airline(self, airline):
        # Select the airline by typing its code in the input field and clicking the first suggestion
        try:
            field_search = self.find_element(By.CSS_SELECTOR, "input[placeholder='Example: AA or American Airlines'], input[name='airlineInput']")
        except:
            print("Element not found")
            return

        field_search.send_keys(airline)

        time.sleep(2)  # Wait for 2 seconds

        try:
            list_container = self.find_element(By.CSS_SELECTOR, "div.basic-menu__MenuContainer-sc-eal1xr-0.dtessv")
        except:
            print("Element not found")
            return

        first_suggestion = list_container.find_element(By.CSS_SELECTOR, "div")  # Click on the first div
        first_suggestion.click()

    def type_flight_number(self, flight_number):
        # Type the flight number in the input field
        try:
            field_search = self.find_element(By.CSS_SELECTOR, "input[type='text'], input[name='flightNumberInputValue']")
        except:
            print("Element not found")
            return

        field_search.send_keys(flight_number)

    def select_date(self, position):
        # Select the flight date by clicking on the corresponding option in the dropdown menu
        date = self.find_element(By.CSS_SELECTOR, "select[name='date']")
        date.click()

        WebDriverWait(self, 3).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "select[name='date'] option")))

        options = self.find_elements(By.CSS_SELECTOR, "select[name='date'] option")
        options[position].click()

    def search(self):
        # Click on the search button
        search_elt = self.find_element(By.CSS_SELECTOR, "button[type='submit']")
        search_elt.click()


    def results(self):
        # Get the scheduled time
        scheduled_time = self.find_elements(By.CLASS_NAME, 'kbHzdx')[0].text
        actual_time = self.find_elements(By.CLASS_NAME, 'kbHzdx')[1].text
        terminal = self.find_element(By.CLASS_NAME, 'ticket__TGBValue-sc-1rrbl5o-16').text
        gate = self.find_elements(By.CLASS_NAME, 'ticket__TGBValue-sc-1rrbl5o-16')[1].text

        results = {
            'scheduled_time': scheduled_time,
            'actual_time': actual_time,
            'terminal': terminal,
            'gate': gate
        }

        return results

        # with open('scraping_results.json', 'w') as f:
        #     json.dump(results, f)

        # table = PrettyTable(
        #     field_names=["scheduled_time", "actual_time", "terminal", "gate"]
        # )
        # table.add_rows([results.values()])
        # print(table)