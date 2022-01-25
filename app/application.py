from pages.sign_in_page import SignIn


class Application:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.sign_in_page = SignIn(self.driver)
        