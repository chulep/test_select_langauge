import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# добавляем парсер для считывания языка и браузера из командной строки
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='es',
                     help="Choose lang")

# фикстура переключающая и передающая браузеры
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nстарт CHROME для теста...")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nстарт FIREFOX для теста...")
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=firefox_profile)
    else:
        print("Указанный браузер не найден".format(browser_name))
    yield browser
    print("\nзакрытие браузера...")
    browser.quit()