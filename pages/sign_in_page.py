from turtle import st
from decouple import config
from pages.base_page import Page

from selenium.webdriver.common.by import By


SING_IN_PAGE = config('SIGNIN_PAGE')


class SignIn(Page):

    AMAZON_LOGO = (By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')
    EMAIL_FIELD = (By.ID, 'ap_email')
    CONTINUE_BTN = (By.ID, 'continue')
    CONDITIONS_OF_USE = (By.CSS_SELECTOR, 'a[href *= "ref=ap_signin_notification_condition_of_use?"]')

    def open_page(self, end_url=SING_IN_PAGE) -> None:
        super().open_page(end_url)

    def locate_amazon_logo(self):
        self.find_element(*self.AMAZON_LOGO)

    def locate_email_field(self):
        self.find_element(*self.EMAIL_FIELD)

    def locate_continue_btn(self):
        expected_text = 'Continue'
        self.verify_text(expected_text, *self.CONTINUE_BTN)

    def locate_conditions_link(self):
        expected_text = 'Conditions of Use'
        self.verify_text(expected_text, *self.CONDITIONS_OF_USE)
