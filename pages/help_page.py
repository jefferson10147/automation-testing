from decouple import config
from selenium.webdriver.common.by import By

from pages.base_page import Page


HELP_PAGE = config('HELP_PAGE')


class HelpPage(Page):
    
    def open_page(self, end_url=HELP_PAGE) -> None:
        super().open_page(end_url)
