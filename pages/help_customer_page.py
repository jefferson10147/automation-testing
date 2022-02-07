from decouple import config
from selenium.webdriver.common.by import By

from pages.base_page import Page


CUSTOMER_PAGE = config('HELP_CUSTOMER')


class HelpCustomer(Page):
    
    WELCOME_TEXT = (By.CSS_SELECTOR ,'.a-section.a-spacing-extra-large.a-spacing-top-extra-large.ss-landing-container h1')
    CARDS = (By.CSS_SELECTOR, '.a-box.self-service-rich-card')
    SEARCH_BAR = (By.ID, 'helpsearch')
    HELP_TOPICS_TITLE = (By.CSS_SELECTOR, '.a-span12.a-column.a-spacing-top-small h1')
    TOPICS = (By.ID, 'category-section')

    def open_help_page(self):
        self.open_page(end_url=CUSTOMER_PAGE)

    def locate_welcome_text(self):
        self.find_element(*self.WELCOME_TEXT)

    def locate_cards(self):
        self.find_elements(*self.CARDS)

    def locate_search_bar(self):
        self.find_element(*self.SEARCH_BAR)

    def locate_topics_title(self):
        self.find_element(*self.HELP_TOPICS_TITLE)

    def locate_topics(self):
        self.find_element(*self.TOPICS)
