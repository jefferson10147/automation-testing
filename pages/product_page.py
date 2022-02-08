from pages.base_page import Page

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from decouple import config


PRODUCT_PAGE = config('PRODUCT_PAGE')


class ProductPage(Page):

    PRICES = (By.CSS_SELECTOR, '.a-price-whole')
    ADD_CART_BTN = (By.ID, 'add-to-cart-button')
    PANTS = (By.CSS_SELECTOR, '#variation_color_name ul li')
    SELECTION_TEXT = (By.CSS_SELECTOR, '#variation_color_name span.selection')

    def open_product_page(self, id):
        end_point = PRODUCT_PAGE + id + '/'
        self.open_page(end_url=end_point)

    def click_in_first_product(self):
        self.click(*self.PRICES)

    def add_to_cart(self):
        self.click(*self.ADD_CART_BTN)

    def verify_colors(self):
        colors = (
            'Black', ' Dark Khaki Brown', 'Dark Indigo/Rinsed', 'Dark Wash',
            'Indigo Wash', 'Light Blue Vintage', 'Light Wash', 'Medium Blue, Vintage',
            'Medium Wash', 'Rinsed', ' Vintage Wash', 'Washed Black',
            'Bright White', 'Dark Khaki Brown', 'Light Khaki Brown', 'Olive',
            'Sage Green', 'Blue, Over Dye', 'Blue, Dip Dye'
        )

        for i in range(len(colors)):
            self.find_elements(*self.PANTS)[i].click()
            self.verify_text(colors[i], *self.SELECTION_TEXT)
