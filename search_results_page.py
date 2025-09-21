from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    PRODUCT_TITLES = (By.CLASS_NAME, "s1Q9rs")

    def get_first_product_name(self):
        return self.find(self.PRODUCT_TITLES).text
