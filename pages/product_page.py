from pages.base_page import Page

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from decouple import config


PRODUCT_PAGE = config('PRODUCT_PAGE')
WHOLEFOODS = config('WHOLEFOODS')


class ProductPage(Page):

    PRICES = (By.CSS_SELECTOR, '.a-price-whole')
    ADD_CART_BTN = (By.ID, 'add-to-cart-button')
    PANTS = (By.CSS_SELECTOR, '#variation_color_name ul li')
    SELECTION_TEXT = (By.CSS_SELECTOR, '#variation_color_name span.selection')
    REGULAR_TEXT = (
        By.CSS_SELECTOR,
        '#wfm-pmd_deals_section .a-size-small.a-color-tertiary.wfm-sales-item-card__regular-price'
    )
    CLOSE_BTN = (By.CSS_SELECTOR, '.glow-toaster-footer span.a-button-inner input')
    RESULT = (
        By.CSS_SELECTOR,
        '.a-section.a-spacing-small.a-spacing-top-small span.a-color-state.a-text-bold'
    )


    def open_product_page(self, id):
        end_point = PRODUCT_PAGE + id + '/'
        self.open_page(end_url=end_point)

    def open_wholefoods_page(self):
        self.open_page(end_url=WHOLEFOODS)

    def click_in_first_product(self):
        self.click(*self.PRICES)

    def click_close_btn(self):
        self.click(*self.CLOSE_BTN)

    def add_to_cart(self):
        self.click(*self.ADD_CART_BTN)

    def verify_colors(self):
        colors = (
            'Black', 'Dark Blue Vintage', 'Dark Indigo/Rinsed', 'Dark Wash',
            'Indigo Wash', 'Light Blue Vintage', 'Light Wash', 'Medium Blue, Vintage',
            'Medium Wash', 'Rinsed', 'Vintage Wash', 'Washed Black',
            'Bright White', 'Dark Khaki Brown', 'Light Khaki Brown', 'Olive',
            'Sage Green', 'Blue, Over Dye', 'Blue, Dip Dye'
        )

        for i in range(len(colors)):
            self.find_elements(*self.PANTS)[i].click()
            self.verify_text(colors[i], *self.SELECTION_TEXT)

    def verfiy_regular_text(self):
        expected_text = 'Regular'
        elements = self.find_elements(*self.REGULAR_TEXT)

        for element in elements:
            self.element_contains_text(expected_text, element)

    def verify_product_in_result_page(self, expected_text):
        self.verify_text(expected_text, *self.RESULT)
