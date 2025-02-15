import sys
import os
import pytest
from playwright.sync_api import sync_playwright
import pages.login_page as login_page
from dotenv import load_dotenv

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Load environment variables from .env file
load_dotenv()

@pytest.fixture(scope="session")
def browser():
    """
    Fixture to launch a new instance of the Chromium browser in non-headless mode.
    The browser instance is closed after the session ends.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.mark.sanity
def test_login(browser):
    """
    Test to perform login using credentials from the .env file.
    It navigates to the URL specified in the .env file, inserts the user credentials,
    and validates a successful login.
    """
    context = browser.new_context()
    page = context.new_page()
    url = os.getenv("URL")
    user = os.getenv("USER")
    password = os.getenv("PASS")

    page.goto(url)
    login_page.login_insert_credentials(page, user, password)
    login_page.validate_successful_login(page)

    context.close()