from decouple import config
from selenium.webdriver.common.by import By

from pages.base_page import Page


T_AND_C_URL = config('T_AND_C_PAGE')


class T_AND_C_PAGE(Page):

    PRIVACY_NOTICE_LINK = (By.CSS_SELECTOR, 'a[href*="/privacy"]')
    PRIVACY_NOTICE_TITLE = (By.CSS_SELECTOR, '.help-content h1')

    def open_page(self, end_url=T_AND_C_URL) -> None:
        super().open_page(end_url)

    def store_original_window(self):
        self.original_window = self.get_original_window()
    
    def click_in_privacy_link(self):
        self.click(*self.PRIVACY_NOTICE_LINK)

    def switch_to_new_window(self):
        self.wait_for_new_window_to_load()
        new_windows = self.get_windows()
        self.switch_to_window(new_windows[-1])

    def verify_private_page_is_open(self):
        expected_text = 'Amazon.com Privacy Notice'
        self.verify_text(expected_text, *self.PRIVACY_NOTICE_TITLE)

    def switch_to_original_page(self):
        self.close_page()
        self.switch_to_window(self.original_window)
