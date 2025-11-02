from unittest.mock import patch, mock_open

from src.json_save import JSONSave
from src.vacancy import Vacancy


@patch('builtins.open', new_callable=mock_open)
@patch('json.load')
def test_read_vacancies(mock_json_load, mock_open_in):
    res = JSONSave("fake_file.json")
    mock_json_load.return_value = [{"name": "Нет названия",
                                    "link": "Нет ссылки", "salary": {"from": "1", "to": "2"},
                                    "description": "Нет описания"},
                                   {"name": "Нет названия",
                                    "link": "Нет ссылки", "salary": {"from": None, "to": None},
                                    "description": "Нет описания"}]
    result = res.read_vacancies()
    assert type(result) is list
    assert result == [Vacancy(**{"name": "Нет названия",
                                 "link": "Нет ссылки", "salary": {"from": "1", "to": "2"},
                                 "description": "Нет описания"}),
                      Vacancy(**{"name": "Нет названия",
                                 "link": "Нет ссылки",
                                 "salary": {},
                                 "description": "Нет описания"})]

#
# @patch('builtins.open', new_callable=mock_open, read_data='[1, 2, 3]')
# @patch('json.load')
# def test_write_vacancies(mock_json_load, mock_open_in):
#     res = JSONSave("fake_file.json")
#     vacancies = [{"name": "Нет названия",
#                   "link": "Нет ссылки", "salary": {"from": "1", "to": "2"},
#                   "description": "Нет описания"}]
#     mock_json_load.return_value = [{"name": "Нет названия",
#                                     "link": "Нет ссылки", "salary": {"from": "1", "to": "2"},
#                                     "description": "Нет описания"},
#                                    {"name": "Нет названия",
#                                     "link": "Нет ссылки", "salary": {"from": None, "to": None},
#                                     "description": "Нет описания"}]
#     result = res.write_vacancies(vacancies)
#     assert type(result) is list
#     assert result == [Vacancy(**{"name": "Нет названия",
#                                  "link": "Нет ссылки", "salary": {"from": "1", "to": "2"},
#                                  "description": "Нет описания"}),
#                       Vacancy(**{"name": "Нет названия",
#                                  "link": "Нет ссылки",
#                                  "salary": {},
#                                  "description": "Нет описания"})]
