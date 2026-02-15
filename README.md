# Дипломный проект: Автоматизация тестирования Кинопоиск (UI + API)

Ссылка на проект: https://github.com/Anna-02071987/kinopoisk-diploma

## Описание проекта
Автоматизированные тесты для веб-приложения Кинопоиск.  
UI-тесты написаны с использованием Selenium и Page Object.  
API-тесты написаны с использованием requests.

## Технологии
Python, Pytest, Selenium, Requests, Allure, Webdriver Manager, Flake8, Python-dotenv

## Структура проекта
- pages / main_page.py
- tests / test_api.py, test_ui.py
- .env (токен, не в Git)
- .flake8
- .gitignore
- conftest.py
- pytest.ini
- requirements.txt
- README.md

## Установка зависимостей
pip install -r requirements.txt

## Настройка API токена
Вариант 1 — через переменную окружения (временно):
$env:API_TOKEN="твой_токен"

Вариант 2 — через .env файл (постоянно):
Создай файл .env и добавь строку:
API_TOKEN=твой_токен

## Запуск тестов
Все тесты:
pytest -v

Только UI:
pytest -m ui -v

Только API:
pytest -m api -v

Allure отчёт:
pytest --alluredir=allure-results
allure serve allure-results

## Проверка кода
flake8 .

## Результаты
- 5 UI тестов
- 5 API тестов
- Page Object паттерн
- Allure отчёты
- Чистый код (flake8)
- Тесты стабильны

## Вывод
Дипломный проект выполнен в соответствии с требованиями. Тесты покрывают UI и API Кинопоиска.
