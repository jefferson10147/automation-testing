from decouple import config

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_PAGE = config('BASE_PAGE')


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = BASE_PAGE

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def input_keys(self, key, *locator):
        e = self.driver.find_element(*locator)
        e.send_keys(key)

    def open_page(self, end_url=''):
        # print(f'{self.base_url}{end_url}')
        self.driver.get(f'{self.base_url}{end_url}')

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def verify_text(self, expected_text, *locator):
        element = self.driver.find_element(*locator)
        self.verify_text_by_element(expected_text, element)

    def element_contains_text(self, expected_text, element):
        actual_text = element.text
        assert expected_text in actual_text, f'Expected {expected_text}, but got {actual_text}'

    def verify_text_by_element(self, expected_text, element):
        actual_text = element.text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    def verify_url_contains_query(self, query):
        assert query in self.driver.current_url, f'{query} not in {self.driver.current_url}'

    def get_original_window(self):
        return self.driver.current_window_handle
