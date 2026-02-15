import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from pages.main_page import MainPage


@allure.story("UI тесты")
@allure.title("UI-01: Поиск фильма — URL содержит kp_query")
@pytest.mark.ui
def test_ui_01_search_movie(driver: WebDriver, ui_base_url: str) -> None:
    with allure.step("Открываем главную страницу"):
        main_page = MainPage(driver)
        main_page.open(ui_base_url)

    with allure.step("Ищем фильм Interstellar"):
        main_page.search("Interstellar")

    with allure.step("Проверяем, что в URL есть параметр kp_query"):
        assert "kp_query=" in driver.current_url


@allure.story("UI тесты")
@allure.title("UI-02: На главной странице есть поле поиска")
@pytest.mark.ui
def test_ui_02_search_field_present(
    driver: WebDriver, ui_base_url: str
) -> None:
    with allure.step("Открываем главную страницу"):
        main_page = MainPage(driver)
        main_page.open(ui_base_url)

    with allure.step("Проверяем, что поле поиска существует"):
        main_page.wait_loaded()
        assert main_page.SEARCH_INPUT is not None


@allure.story("UI тесты")
@allure.title("UI-03: Заголовок страницы не пустой")
@pytest.mark.ui
def test_ui_03_title_not_empty(driver: WebDriver, ui_base_url: str) -> None:
    with allure.step("Открываем главную страницу"):
        main_page = MainPage(driver)
        main_page.open(ui_base_url)

    with allure.step("Проверяем, что title не пустой"):
        assert driver.title.strip() != ""


@allure.story("UI тесты")
@allure.title("UI-04: Открытие карточки фильма из результатов поиска")
@pytest.mark.ui
def test_ui_04_open_movie_from_results(
    driver: WebDriver, ui_base_url: str
) -> None:
    with allure.step("Открываем главную страницу"):
        main_page = MainPage(driver)
        main_page.open(ui_base_url)

    with allure.step("Ищем фильм Interstellar"):
        main_page.search("Interstellar")

    with allure.step("Открываем первый результат поиска"):
        main_page.wait_results()
        first_link = main_page.results()[0]
        first_link.click()

    with allure.step("Проверяем, что URL содержит /film/"):
        assert "/film/" in driver.current_url


@allure.story("UI тесты")
@allure.title("UI-05: Страница загружается, HTML не пустой")
@pytest.mark.ui
def test_ui_05_page_source_not_empty(
    driver: WebDriver, ui_base_url: str
) -> None:
    with allure.step("Открываем главную страницу"):
        main_page = MainPage(driver)
        main_page.open(ui_base_url)

    with allure.step("Проверяем, что HTML код страницы больше 1000 символов"):
        assert len(driver.page_source) > 1000
