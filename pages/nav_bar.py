from pages.base_page import Page

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NavBar(Page):

    SEARCH_BAR = (By.ID, 'twotabsearchtextbox')
    CART_COUNT = (By.ID, 'nav-cart-count')
    DEPARMENTS_DROPDOWN = (By.ID, 'searchDropdownBox')
    VIDEOGAMES_OPTION = (
        By.CSS_SELECTOR, '#searchDropdownBox option[value="search-alias=videogames-intl-ship"]')

    def input_into_search_bar(self, text: str):
        self.input_text(text, *self.SEARCH_BAR)
        self.input_keys(Keys.ENTER, *self.SEARCH_BAR)

    def verify_cart_count(self, number_of_items='1'):
        self.verify_text(number_of_items, *self.CART_COUNT)

    def click_in_dropdown(self):
        self.click(*self.DEPARMENTS_DROPDOWN)

    def click_in_videogames_option(self):
        self.wait_for_element_click(*self.VIDEOGAMES_OPTION)
