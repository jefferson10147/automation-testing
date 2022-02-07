from pages.base_page import Page

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NavBar(Page):

    SEARCH_BAR = (By.ID, 'twotabsearchtextbox')

    def input_into_search_bar(self, text: str):
        self.input_text(text, *self.SEARCH_BAR)
        self.input_keys(Keys.BACK_SPACE, *self.SEARCH_BAR)
