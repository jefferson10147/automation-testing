from decouple import config
from pages.base_page import Page


T_AND_C_URL = config('T_AND_C_PAGE')


class T_AND_C_PAGE(Page):
    
    def open_page(self, end_url=T_AND_C_URL) -> None:
        super().open_page(end_url)
