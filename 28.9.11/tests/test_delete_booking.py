import pytest
import requests
from api.api import auth_token, create_booking

# тесты для удаления бронирования

@pytest.mark.parametrize('auth_token, create_booking, content_type, wait_status',
    [(auth_token(), create_booking(auth_token), 'application/json', 201),      # валидные данные
     ('negativ557token', create_booking(auth_token), 'application/json', 403), # несуществующий токен и негативный код-статус
     (auth_token(), '-2', 'application/json', 405),                            # несуществующий id бронирования
     (auth_token(), create_booking(auth_token), '', 415),                      # пустой content_type и неверный статус-код - БАГ
     ("", "", 'application/json', 405)                                         # пустые токен и id - БАГ тест проходит с любым статус-кодом
     ])


def test_delete_booking(auth_token, create_booking, content_type, wait_status):

    url = f'https://restful-booker.herokuapp.com/booking/{create_booking}'
    headers = {
        'Content-Type': 'application/json',
        'Cookie': f'token={auth_token}'
    }
    response = requests.delete(url, headers=headers) # ответ содержит данные о выполненном запросе
    if response.status_code == 201:
        assert response.status_code == wait_status, f'Запрос на удаление заказа выполнен, статус-код {response.status_code}'
        assert response.text == 'Created', 'Delete booking response should contain "Created"'
        print("Заказ удален")
    elif response.status_code == 403:
        assert response.status_code == wait_status, f'Запрос на удаление заказа не выполнен, статус-код {response.status_code}'
        assert response.text == 'Forbidden', 'Delete booking response should contain "Created"'
        print("Проблема на стороне клиента, заказ не удален, код 403")
    elif response.status_code == 405:
        assert response.status_code == wait_status, f'Запрос на удаление заказа не выполнен, статус-код {response.status_code}'
        assert response.text == 'Method Not Allowed', 'Delete booking response should contain "Created"'
        print("Проблема на стороне клиента, заказ не удален, код 405")
    elif response.status_code == 415:
        assert response.status_code == wait_status, f'Запрос на удаление заказа не выполнен, статус-код {response.status_code}'
        assert response.text == 'Unsupported Media Type', 'Delete booking response should contain "Created"'
        print("Проблема на стороне клиента, заказ не удален, код 415")
