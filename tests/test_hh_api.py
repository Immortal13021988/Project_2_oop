from unittest.mock import patch

from requests import Response

from src.hh_api import HHApi


@patch("requests.get")
def test_connect(mock_get):
    hh = HHApi()
    mock_resp = mock_get.return_value
    mock_resp.status_code = 200
    mock_resp.json.return_value = {"items": [1, 2]}
    assert hh.get_vacancies("test", 1) == [1, 2]



