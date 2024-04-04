import pytest

from playwright.sync_api import Page, expect

from helpers.variables import main_url

from pages.login_module import Login


@pytest.fixture
def login(page: Page):
    login = Login(page, main_url)
    page.goto(login.login_page)

    page.fill('input[data-test="username"]', login.username)
    page.fill('input[data-test="password"]', login.password)

    page.click('input[data-test="login-button"]')

    return login


@pytest.mark.logout
def test_login_and_logout(page: Page, login):
    page.click('button[id="react-burger-menu-btn"]')
    page.click('a[id="logout_sidebar_link"]')

    expect(page.locator('div[data-test="login-container"]')).to_be_visible()

