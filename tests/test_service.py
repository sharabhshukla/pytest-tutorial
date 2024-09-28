import pytest
from src.service import get_user_from_db
import unittest.mock as mock

@mock.patch("src.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = mock_get_user_from_db(1)

    assert user_name == "Mocked Alice"


#



