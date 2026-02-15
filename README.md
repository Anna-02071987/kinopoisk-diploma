# Дипломный проект: Автоматизация тестирования Кинопоиск (UI + API)

**Ссылка на проект:** [kinopoisk-diploma](https://github.com/Anna-02071987/kinopoisk-diploma)

## Описание проекта
Проект представляет собой автоматизированные тесты для веб-приложения Кинопоиск. Реализованы UI-тесты (Selenium) и API-тесты (requests) с использованием Page Object паттерна.

## Технологии
- Python 3.14
- Pytest
- Selenium
- Requests
- Allure Reports
- Webdriver Manager
- Flake8
- Python-dotenv

## Структура проекта

```
kinopoisk-diploma/
├── pages/ # Page Objects
│ └── main_page.py
├── tests/ # Тесты
│ ├── test_api.py
│ └── test_ui.py
├── .env # Токен (не в Git)
├── .flake8 # Настройки flake8
├── .gitignore # Игнорируемые файлы
├── conftest.py # Фикстуры
├── pytest.ini # Конфигурация pytest
├── requirements.txt # Зависимости
└── README.md # Описание проекта
```

## Установка зависимостей
```bash
pip install -r requirements.txt

Настройка API токена
Вариант 1 - через переменную окружения (временно):
$env:API_TOKEN="RPGCR3Q-8MQMKD4-GKGK204-8QGES6A"

Вариант 2 - через .env файл (постоянно):
Создай файл .env в корне проекта и добавь:
API_TOKEN=твой_токен

Запуск тестов
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
✅ Page Object паттерн
✅ Allure отчеты
✅ Чистый код (flake8)
✅ Все тесты стабильно проходят

Вывод
Дипломный проект выполнен в полном соответствии с требованиями. Автоматизированные тесты покрывают как UI, так и API функциональность Кинопоиска. Код соответствует стандартам PEP8, стабильно проходит при многократном запуске.
