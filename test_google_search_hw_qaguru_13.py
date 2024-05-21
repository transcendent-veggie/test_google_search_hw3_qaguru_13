import pytest
from selene import browser, be, have


@pytest.fixture()
def browser_open():
    browser.config.window_height = 800
    browser.config.window_width = 800
    print('\nbrowser opened')
    yield
    browser.quit()
    print('\nbrowser closed')


@pytest.fixture()
def browser_goto_google(browser_open):
    browser.open('https://www.google.com/')


@pytest.fixture()
def browser_goto_duck(browser_open):
    browser.open('https://duckduckgo.com/')


@pytest.fixture()
def search_google(browser_goto_google):
    browser.element('[name="q"]').should(be.blank).type('wikipedia').press_enter()


@pytest.fixture()
def search_duck(browser_goto_duck):
    browser.element('#searchbox_input').should(be.blank).type('карфаген').press_enter()


def test_search_google(search_google):
    assert browser.element('[id="search"]').should(have.text('Wikipedia is a free online encyclopedia'))


def test_search_duck(search_duck):
    assert browser.element('#react-layout').should(have.text('финикийское государство'))


def test_search_negative_results(search_google):
    assert browser.element('#search').should(have.text('asdasdasdasd'))
