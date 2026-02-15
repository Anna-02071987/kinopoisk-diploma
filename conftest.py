import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os


def pytest_addoption(parser):
    """Фикстура для добавления параметров командной строки"""
    parser.addoption(
        "--browser", action="store", default="chrome",
        help="Browser to run tests"
    )
    parser.addoption(
        "--headless", action="store_true",
        help="Run browser in headless mode"
    )


@pytest.fixture(scope="session")
def base_url() -> str:
    """Базовый URL для API тестов"""
    return "https://api.kinopoisk.dev/v1.4"


@pytest.fixture(scope="session")
def ui_base_url() -> str:
    """Базовый URL для UI тестов"""
    return "https://www.kinopoisk.ru"


@pytest.fixture(scope="session")
def api_timeout() -> int:
    """Таймаут для API запросов"""
    return 10


@pytest.fixture(scope="session")
def api_token() -> str:
    """Токен для API запросов (берется из переменной окружения)"""
    token = os.getenv("API_TOKEN")
    if not token:
        pytest.fail("API_TOKEN не установлен в переменных окружения")
    return token


@pytest.fixture(scope="session")
def api_session(api_token: str) -> requests.Session:
    """Сессия для API запросов с токеном авторизации"""
    session = requests.Session()
    session.headers.update({
        "X-API-KEY": api_token,
        "accept": "application/json"
    })
    return session


@pytest.fixture(scope="function")
def driver(request, ui_base_url: str) -> webdriver.Chrome:
    """
    Фикстура для создания и закрытия драйвера браузера.
    Поддерживает аргументы --browser и --headless.
    """
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        options = Options()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")

        # Используем webdriver-manager для автоматической загрузки драйвера
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")

    driver.get(ui_base_url)
    driver.maximize_window()

    yield driver

    # Закрываем браузер после теста
    driver.quit()
