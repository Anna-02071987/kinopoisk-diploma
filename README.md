# Дипломный проект: Автоматизация тестирования Кинопоиск (UI + API)

## Описание проекта
Проект представляет собой автоматизированные тесты для веб-приложения Кинопоиск. Реализованы UI-тесты (Selenium) и API-тесты (requests).

## Технологии
- Python 3.14
- Pytest
- Selenium
- Requests
- Allure Reports
- Webdriver Manager
- Flake8

## Структура проекта

kinopoisk-diploma/
├── pages/ # Page Objects (для UI тестов)
├── tests/ # Тесты
│ ├── test_ui.py # UI-тесты
│ └── test_api.py # API-тесты
├── conftest.py # Фикстуры и настройки
├── pytest.ini # Конфигурация pytest
├── requirements.txt # Зависимости
└── README.md # Описание проекта


## Запуск тестов

### Установка зависимостей
```bash
pip install -r requirements.txt

Настройка API токена
$env:API_TOKEN="RPGCR3Q-8MQMKD4-GKGK204-8QGES6A"

Запуск всех тестов
pytest -v

Запуск только UI тестов
pytest -m ui -v

Запуск только API тестов
pytest -m api -v

Запуск с отчетом Allure
pytest --alluredir=allure-results
allure serve allure-results

Проверка кода (flake8)
flake8 .

Результаты
✅ 5 UI тестов

✅ 5 API тестов

✅ Все тесты стабильно проходят