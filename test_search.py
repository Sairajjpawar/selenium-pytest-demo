import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_flipkart_search(driver):
    home = HomePage(driver)
    results = SearchResultsPage(driver)

    home.open("https://www.flipkart.com")
    # Close login popup if it appears
    try:
        driver.find_element("xpath", "//button[contains(text(),'✕')]").click()
    except:
        pass

    home.search_product("laptop")
    first_result = results.get_first_product_name()

    print("First search result:", first_result)
    assert "Laptop" in first_result or first_result != ""

