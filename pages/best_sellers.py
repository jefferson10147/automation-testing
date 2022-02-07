from pages.base_page import Page

from decouple import config
from selenium.webdriver.common.by import By


BEST_SELLERS_PAGE = config('BEST_SELLERS')

class BestSellers(Page):
    
    BEST_SELLERS_LINKS = (By.CSS_SELECTOR, '[href *= "/ref=zg_bs_tab"]')

    def open_best_sellers_page(self):
        self.open_page(end_url=BEST_SELLERS_PAGE)

    def locate_elements(self):
        self.elements = self.find_elements(*self.BEST_SELLERS_LINKS)

    def verify_links(self, numbers_of_links=5):
        current_number_of_links = len(self.elements)
        assert numbers_of_links == current_number_of_links, f'Expected {numbers_of_links} but got {current_number_of_links}'
