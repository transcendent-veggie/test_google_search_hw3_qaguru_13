from selene import browser, be, have


def test_search_google(browser_open):
    browser.open('https://www.google.com/')
    browser.element('[name="q"]').should(be.blank).type('wikipedia').press_enter()
    assert browser.element('[id="search"]').should(have.text('Wikipedia is a free online encyclopedia'))


'''def test_search_duck(search_duck):
    browser.open('https://duckduckgo.com/')
    browser.element('#searchbox_input').should(be.blank).type('карфаген').press_enter()
    assert browser.element('#react-layout').should(have.text('финикийское государство'))
'''


def test_search_negative_results(browser_open):
    browser.open('https://www.google.com/')
    browser.element('[name="q"]').should(be.blank).type('-тест').press_enter()
    assert browser.element('#botstuff').should(have.text(' ничего не найдено.'))
