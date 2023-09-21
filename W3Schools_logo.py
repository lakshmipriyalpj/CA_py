import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture
def driver():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    # Set an implicit wait to handle dynamic content loading
    driver.implicitly_wait(10)
    # Yield the driver object to the test
    yield driver
    # After the test, close the browser
    driver.quit()
def test_w3schools_logo_presence(driver):
    # Open the W3Schools website
    driver.get("https://www.w3schools.com/")

    # Find the logo element by its XPath (you can use other locators if needed)
    logo_element = driver.find_element(By.XPATH, '//a[@id="w3-logo"]')

    # Verify if the logo element is present on the page
    assert logo_element.is_displayed(), "W3Schools logo is not present on the page"
