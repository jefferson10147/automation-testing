from turtle import st
from decouple import config
from pages.base_page import Page


SING_IN_PAGE = config('SING_IN_PAGE')


class SignIn(Page):

    def open_page(self, end_url=SING_IN_PAGE) -> None:
        super().open_page(end_url)
