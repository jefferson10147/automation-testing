from pages.base_page import Page

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NavBar(Page):

    SEARCH_BAR = (By.ID, 'twotabsearchtextbox')
    CART_COUNT = (By.ID, 'nav-cart-count')

    def input_into_search_bar(self, text: str):
        self.input_text(text, *self.SEARCH_BAR)
        self.input_keys(Keys.ENTER, *self.SEARCH_BAR)

    def verify_cart_count(self, number_of_items='1'):
        self.verify_text(number_of_items, *self.CART_COUNT)
