import json
from abc import ABC, abstractmethod

from src.vacancy import Vacancy
from src.hh_api import HHApi


class AbstractJson(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def write_vacancies(self, vacancies):
        pass

    @abstractmethod
    def read_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass


class JSONSave(AbstractJson):
    """Класс взаимодействия с JSON"""

    def __init__(self, filename: str = "../data/vacancies.json"):
        """Инициализация класса"""
        self.__filename = filename

    def read_vacancies(self) -> list:
        """Метод получения данных из JSON файла"""
        try:
            with open(self.__filename, encoding="utf-8") as f:
                data = json.load(f)
            vacancies = []
            for vacancy in data:
                vacancies.append(Vacancy(**vacancy))
            return vacancies
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def write_vacancies(self, vacancies: list):
        """Метод записи JSON файла"""
        with open(self.__filename, encoding="utf-8") as f:
            data = json.load(f)
        for vacancy in vacancies:
            vacancy_name = vacancy.get("name")
            if not any(vacancy_name == vac.get("name") for vac in data):
                data.append(
                    {
                        "name": vacancy["name"],
                        "link": vacancy["alternate_url"],
                        "salary": vacancy["salary"],
                        "description": vacancy["snippet"]["requirement"],
                    }
                )
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def delete_vacancies(self):
        """Метод очистки файла с сохранением JSON формата"""
        with open(self.__filename, "w") as f:
            json.dump([], f)


if __name__ == "__main__":
    hh = HHApi()
    vacancy_api = hh.get_vacancies("java")
    for vac in vacancy_api:
        print(vac.get("name"))
    json_serv = JSONSave()
    json_serv.write_vacancies(vacancy_api)