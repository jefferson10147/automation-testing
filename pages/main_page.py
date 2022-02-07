from msilib.schema import Class
from pages.base_page import Page

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MainPage(Page):

    CART = (By.ID, 'nav-cart-count-container')
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty h2')
    SEARCH_BAR = (By.ID, 'twotabsearchtextbox')

    def open_amazon_main_page(self):
        self.open_page()

    def click_in_cart_icon(self):
        self.click(*self.CART)

    def verify_empty_cart_text(self):
        expected_text = 'Your Amazon Cart is empty'
        self.verify_text(expected_text, *self.EMPTY_CART_TEXT)

    def input_into_search_bar(self, text: str):
        self.input_text(text, *self.SEARCH_BAR)
        self.input_keys(Keys.BACK_SPACE, *self.SEARCH_BAR)
