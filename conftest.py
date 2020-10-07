import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="Choose language")
    parser.addoption('--browser', action='store', default="chrome",\
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    language = request.config.getoption("language")
    languages_list = ["de", "ar", "ca", "cs", "da","en", "en-gb", "el", "es", "fi", "fr", "it", "ko", "nl", "pl", "pt", "pt-br", "ro", "ru", "sk", "uk", "zh-hans"]
    if language not in languages_list:
        raise pytest.UsageError("--language should be chosen from the existing list")

    browser_name = request.config.getoption("browser")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
