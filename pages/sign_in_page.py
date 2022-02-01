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
    PRIVACY_NOTICE = (By.CSS_SELECTOR, 'a[href *= "ref=ap_signin_notification_privacy_notice?"]')
    NEED_HELP = (By.CSS_SELECTOR, 'a span.a-expander-prompt')

    def open_page(self, end_url=SING_IN_PAGE) -> None:
        super().open_page(end_url)

    def locate_amazon_logo(self) -> None:
        self.find_element(*self.AMAZON_LOGO)

    def locate_email_field(self) -> None:
        self.find_element(*self.EMAIL_FIELD)

    def locate_continue_btn(self) -> None:
        expected_text = 'Continue'
        self.verify_text(expected_text, *self.CONTINUE_BTN)

    def locate_conditions_link(self) -> None:
        expected_text = 'Conditions of Use'
        self.verify_text(expected_text, *self.CONDITIONS_OF_USE)

    def locate_privacy_notice_link(self) -> None:
        expected_text = 'Privacy Notice'
        self.verify_text(expected_text, *self.PRIVACY_NOTICE)

    def locate_need_help_link(self) -> None:
        expected_text = 'Need help?'
        self.verify_text(expected_text, *self.NEED_HELP)
