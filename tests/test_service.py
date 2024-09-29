from urllib.error import HTTPError

import pytest
import requests

from src.service import get_user_from_db, get_users
import unittest.mock as mock

@mock.patch("src.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = mock_get_user_from_db(1)

    assert user_name == "Mocked Alice"


@mock.patch("requests.get")
def test_get_users_from_api(mock_get_users):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'id': 1, "name": "JagatGuru"}
    mock_get_users.return_value = mock_response
    data = get_users()
    assert data == {'id': 1, "name": "JagatGuru"}


@mock.patch("requests.get")
def test_get_users_fail(mock_get_response):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get_response.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        get_users()





#



