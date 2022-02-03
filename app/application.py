from pages.sign_in_page import SignIn
from pages.help_page import HelpPage


class Application:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.sign_in_page = SignIn(self.driver)
        self.help_page = HelpPage(self.driver)
