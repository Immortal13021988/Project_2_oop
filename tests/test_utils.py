from src.utils import vacancies_by_name, top_vacancies
from src.vacancy import Vacancy


def test_vacancies_by_name_0():
    vacancy_obj = Vacancy(**{"name": "Нет названия",
                             "link": "Нет ссылки", "salary": {"from": "1", "to": "2"},
                             "description": "Нет описания"})

    assert vacancy_obj.__str__() == ("Название: Нет названия, Ссылка: Нет ссылки, Зарплата от: 1, до: 2, "
                                     "Описание: Нет описания")


def test_vacancies_by_name():
    vacancies = [{"name": "Нет названия",
                  "alternate_url": "Нет ссылки", "salary": {"from": "1", "to": "2"},
                  "snippet": {"Нет описания": "requirement"}}]
    vacancies_by_name(vacancies)


def test_vacancies_by_name_not():
    vacancies = []
    vacancies_by_name(vacancies)


def test_vacancies_by_name_ex():
    vacancies = "[{}]"
    vacancies_by_name(vacancies)  # Проверяем на ошибку


def test_top_vacancies():
    vacancies = [Vacancy(**{"name": "Нет названия",
                            "link": "Нет ссылки", "salary": {"from": 3, "to": 4},
                            "description": "Нет описания"}),
                 Vacancy(**{"name": "Нет названия",
                            "link": "Нет ссылки",
                            "salary": {"from": 5, "to": 6},
                            "description": "Нет описания"}),
                 Vacancy(**{"name": "Нет названия",
                            "link": "Нет ссылки",
                            "salary": {"from": 1, "to": 2},
                            "description": "Нет описания"})
                 ]
    assert top_vacancies(vacancies) == [Vacancy(**{"name": "Нет названия",
                                                   "link": "Нет ссылки", "salary": {"from": 1, "to": 2},
                                                   "description": "Нет описания"}),
                                        Vacancy(**{"name": "Нет названия",
                                                   "link": "Нет ссылки",
                                                   "salary": {"from": 3, "to": 4},
                                                   "description": "Нет описания"}),
                                        Vacancy(**{"name": "Нет названия",
                                                   "link": "Нет ссылки",
                                                   "salary": {"from": 5, "to": 6},
                                                   "description": "Нет описания"})
                                        ]
