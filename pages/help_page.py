from decouple import config
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import Page


HELP_PAGE = config('HELP_PAGE')


class HelpPage(Page):
    
    SEARCH_BAR = (By.ID, 'helpsearch')
    CANCEL_ITEMS_TEXT = (By.CSS_SELECTOR, 'div.help-content h1')

    def open_page(self, end_url=HELP_PAGE) -> None:
        super().open_page(end_url)

    def search_for_cancel_orders(self):
        text = 'Cancel order'
        self.input_text(text, *self.SEARCH_BAR)
        self.input_keys(Keys.RETURN, *self.SEARCH_BAR)

    def verify_cancel_order_text(self):
        text = 'Cancel Items or Orders'
        self.wait_for_element_appear(*self.CANCEL_ITEMS_TEXT)
        self.verify_text(text, *self.CANCEL_ITEMS_TEXT)
