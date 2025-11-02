from abc import ABC, abstractmethod

import requests


class AbstractAPI(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def _connect(self, text):
        pass

    @abstractmethod
    def get_vacancies(self, text):
        pass


class HHApi(AbstractAPI):
    """Класс взаимодействия с hh.ru"""

    def __init__(self, page=0):
        """Инициализация класса"""
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {"page": page, "per_page": 30}

    def _connect(self, text):
        """Получение данных с hh.ru"""
        try:
            self.__params["text"] = text
            response = requests.get(self.__url, params=self.__params)
            response.raise_for_status()
            return response
        except requests.RequestException as e:  # pragma no cover
            print(f"Ошибка при подключении к API: {e}")
            return None

    def get_vacancies(self, text, page=5) -> list[dict]:
        """Метод получения и обработки данных о вакансиях"""
        all_vacancies = []
        while self.__params["page"] < page:
            vacancies = self._connect(text).json()["items"]
            all_vacancies.extend(vacancies)
            self.__params["page"] += 1
        return all_vacancies


if __name__ == "__main__":
    hh = HHApi()
    print(hh.get_vacancies("python"))
