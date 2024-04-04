from playwright.sync_api import Page


class Login:
    def __init__(self, page: Page, url):
        self._page = page
        self._url = url
        self._username = 'standard_user'
        self._password = 'secret_sauce'

    @property
    def login_page(self):
        return self._url

    @login_page.setter
    def login_page(self, new_url):
        if not isinstance(new_url, str):
            raise ValueError("Inserted URL is not a string")
        self._url = new_url

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if not isinstance(new_username, str):
            raise ValueError("Username must be a string")
        self._username = new_username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        if not isinstance(new_password, str):
            raise ValueError("Password must be a string")
        self._password = new_password
