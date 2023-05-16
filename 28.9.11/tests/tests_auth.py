import pytest
import requests
from pydantic import ValidationError
from objclass.classes import AuthRequest

#тесты для создания токена
@pytest.mark.parametrize('username, password, headers', [
    ('admin', 'password123', {"Content-Type": "application/json"}),    # валидные данные
    ('admin', 'password123', {"Content-Type": ""}),                    # Content-Type без значение - БАГ
    ('admin', 'password123', {}),                                      # нет третьего параметра
    ('', '', {"Content-Type": "application/json"}),                    # пустые первые два параметра - БАГ
    ('negative', 'negative123', {"Content-Type": "application/json"}), # несуществующие значение первых двух параметров - БАГ
    ('15984257', 'password123', {"Content-Type": "application/json"}), # число в параметре первого значения - БАГ
])
def test_auth_request(username, password, headers):
    global data
    url = "https://restful-booker.herokuapp.com/auth"

    try:
        data = AuthRequest(username=username, password=password)
    except ValidationError as e:
        if username == '' and password == '': # если параметры пустые, возвращается сообщение об ошибке
            assert str(e) == "1 validation error for AuthRequest\nusername\n  " \
                             "field required (type=value_error.missing)\npassword\n  " \
                             "field required (type=value_error.missing)"
        else:
            pytest.fail(f"Не удалось проверить данные запроса: {e}")

    response = requests.post(url, headers=headers, json=data.dict()) # ответ содержит данные о выполненном запросе

    assert response.status_code == 200
    print(f"Запрос выполнен со статус-кодом {response.status_code}")
    if "reason" in response.json() and response.json()["reason"] == "Bad credentials":
        assert "token" not in response.json(), "Недопустимые учетные данные"
        print("Недопустимые учетные данные")
    else:
        assert "token" in response.json(), "Ответ содержит token"
        print("Ответ содержит токен")