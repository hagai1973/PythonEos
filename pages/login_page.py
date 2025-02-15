# login_page.py
"""
This module contains functions to interact with the login page of the application.
It provides methods to insert user credentials and validate a successful login.

Functions:
    login_insert_credentials(page: Page, user: str, password: str)
        Inserts the user credentials into the login form and submits it.

    validate_successful_login(page: Page)
        Validates that the login was successful by checking the URL.
"""

from playwright.sync_api import Page

def login_insert_credentials(page: Page, user: str, password: str):
    """
    Inserts the user credentials into the login form and submits it.

    Args:
        page (Page): The Playwright page object representing the browser page.
        user (str): The username or email to be inserted into the login form.
        password (str): The password to be inserted into the login form.
    """
    page.fill('input#\\:r1\\:', user)
    page.fill('input#\\:r2\\:', password)
    page.click('button[type="submit"]')

def validate_successful_login(page: Page):
    """
    Validates that the login was successful by checking the URL.

    Args:
        page (Page): The Playwright page object representing the browser page.

    Raises:
        AssertionError: If the current URL does not match the expected URL after login.
    """
    assert page.url == "https://web.eos.bnk-il.com/dashboard"  # Example URL after login