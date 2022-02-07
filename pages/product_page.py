from pages.base_page import Page

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ProductPage(Page):

    PRICES = (By.CSS_SELECTOR, '.a-price-whole')
    ADD_CART_BTN =(By.ID, 'add-to-cart-button')

    def click_in_first_product(self):
        self.click(*self.PRICES)

    def add_to_cart(self):
        self.click(*self.ADD_CART_BTN)
