import allure
import pytest
import requests


@allure.story("API тесты")
@allure.title("API-01: Поиск фильма на кириллице")
@pytest.mark.api
def test_api_pos_01_search_cyrillic(api_session, base_url, api_timeout):
    """Проверяем поиск фильма на русском языке"""
    with allure.step("Отправляем запрос на поиск фильма 'Интерстеллар'"):
        response = api_session.get(
            f"{base_url}/movie/search",
            params={"query": "Интерстеллар"},
            timeout=api_timeout
        )

    with allure.step("Проверяем, что статус ответа 200"):
        assert response.status_code == 200

    with allure.step("Проверяем, что в ответе есть результаты"):
        data = response.json()
        assert "docs" in data
        assert len(data["docs"]) > 0


@allure.story("API тесты")
@allure.title("API-02: Поиск фильма на латинице")
@pytest.mark.api
def test_api_pos_02_search_latin(api_session, base_url, api_timeout):
    """Проверяем поиск фильма на английском языке"""
    with allure.step("Отправляем запрос на поиск фильма 'Interstellar'"):
        response = api_session.get(
            f"{base_url}/movie/search",
            params={"query": "Interstellar"},
            timeout=api_timeout
        )

    with allure.step("Проверяем статус ответа"):
        assert response.status_code == 200

    with allure.step("Проверяем наличие результатов"):
        data = response.json()
        assert "docs" in data
        assert len(data["docs"]) > 0


@allure.story("API тесты")
@allure.title("API-03: Получение фильма по ID")
@pytest.mark.api
def test_api_pos_03_movie_by_id(api_session, base_url, api_timeout):
    """Проверяем получение фильма по его идентификатору"""
    with allure.step("Сначала ищем фильм, чтобы получить его ID"):
        search = api_session.get(
            f"{base_url}/movie/search",
            params={"query": "Interstellar"},
            timeout=api_timeout
        )
        assert search.status_code == 200
        docs = search.json().get("docs", [])
        assert docs, "Фильм не найден"
        movie_id = docs[0].get("id")
        assert movie_id is not None

    with allure.step(f"Получаем фильм по ID: {movie_id}"):
        movie = api_session.get(
            f"{base_url}/movie/{movie_id}",
            timeout=api_timeout
        )

    with allure.step("Проверяем, что ID совпадает"):
        assert movie.status_code == 200
        assert movie.json().get("id") == movie_id


@allure.story("API тесты")
@allure.title("API-04: Запрос без токена (должен быть 401/403)")
@pytest.mark.api
def test_api_neg_01_no_token(base_url, api_timeout):
    """Проверяем, что без токена API не работает"""
    with allure.step("Создаем сессию без токена"):
        session = requests.Session()
        session.headers.update({"accept": "application/json"})

    with allure.step("Отправляем запрос без токена"):
        response = session.get(
            f"{base_url}/movie/search",
            params={"query": "Interstellar"},
            timeout=api_timeout
        )

    with allure.step("Проверяем, что статус ошибки (401 или 403)"):
        assert response.status_code in (401, 403)


@allure.story("API тесты")
@allure.title("API-05: Неправильный метод запроса (PUT)")
@pytest.mark.api
def test_api_neg_02_wrong_method_put(api_session, base_url, api_timeout):
    """Проверяем, что PUT запрос не работает"""
    with allure.step("Отправляем PUT запрос вместо GET"):
        response = api_session.put(
            f"{base_url}/movie/search",
            params={"query": "Interstellar"},
            timeout=api_timeout
        )

    with allure.step("Проверяем, что вернулась ошибка 400, 404 или 405"):
        assert response.status_code in (400, 404, 405)
