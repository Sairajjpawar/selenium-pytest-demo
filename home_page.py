from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    SEARCH_BOX = (By.NAME, "q")
    SEARCH_BUTTON = (By.CLASS_NAME, "L0Z3Pu")

    def search_product(self, product_name):
        self.type(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BUTTON)
