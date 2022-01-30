from turtle import st
from decouple import config
from pages.base_page import Page

from selenium.webdriver.common.by import By


SING_IN_PAGE = config('SIGNIN_PAGE')


class SignIn(Page):

    AMAZON_LOGO = (By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

    def open_page(self, end_url=SING_IN_PAGE) -> None:
        super().open_page(end_url)

    def locate_amazon_logo(self):
        self.find_element(*self.AMAZON_LOGO)
        