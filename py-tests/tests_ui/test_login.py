import re

import pytest

from playwright.sync_api import Page, expect

from helpers.variables import main_url

from pages.login_module import Login


@pytest.fixture
def login(page: Page):
    login = Login(page, main_url)
    return login


def test_login_to_page_title(page: Page, login):

    page.goto(login.login_page)

    # # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Swag Labs"))


def test_login_to_new_page_title(page: Page, login):
    login.login_page = 'https://google.com'

    page.goto(login.login_page)

    # # Expect a title "to contain" a new substring.
    expect(page).to_have_title(re.compile("Google"))


# you can run this test using mark
# pytest -m login -v
@pytest.mark.login
def test_login_to_page_with_standard_user(page: Page, login):
    page.goto(login.login_page)

    page.fill('input[data-test="username"]', login.username)
    page.fill('input[data-test="password"]', login.password)

    page.click('input[data-test="login-button"]')

    expect(page.locator('div[data-test="primary-header"]')).to_be_visible()


# you can run this test using mark
# pytest -m login_locked -v
@pytest.mark.login_locked
def test_login_to_page_with_locked_user(page: Page, login):
    page.goto(login.login_page)
    login.username = "locked_out_user"

    page.fill('input[data-test="username"]', login.username)
    page.fill('input[data-test="password"]', login.password)

    page.click('input[data-test="login-button"]')

    expect(page.locator('button[data-test="error-button"]')).to_be_visible()