from pages.sign_in_page import SignIn
from pages.help_page import HelpPage
from pages.main_page import MainPage


class Application:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.sign_in_page = SignIn(self.driver)
        self.help_page = HelpPage(self.driver)
        self.main_page = MainPage(self.driver)
