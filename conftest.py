import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_open():
    browser.config.window_height = 800
    browser.config.window_width = 800
    print('\nbrowser opened')
    yield
    browser.quit()
    print('\nbrowser closed')
