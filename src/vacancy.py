class Vacancy:
    """Класс для работы с вакансиями, валидация и сравнения"""
    __slots__ = ("name", "link", "description", "salary_from", "salary_to")

    def __init__(self, name, link, salary, description):
        """Инициализация класса"""

        self.name = name
        self.link = link
        self.description = description
        self.__validate(salary)

    def __validate(self, salary):
        """Валидация зарплат"""
        if salary:
            self.salary_from = salary["from"] if salary["from"] else 0
            self.salary_to = salary["to"] if salary["to"] else 0
        else:
            self.salary_from = 0
            self.salary_to = 0

    def __eq__(self, other):  # метод меньше
        """Метод сравнения (<)"""
        return self.name == other.name and self.link == other.link and self.description == other.description

    def __lt__(self, other):  # метод меньше
        """Метод сравнения (<)"""
        return self.salary_from < other.salary_from

    def __str__(self):
        """Передача строкового значения вакансии"""
        return (
            f"Название: {self.name}, Ссылка: {self.link}, Зарплата от: {self.salary_from}, до: {self.salary_to}, "
            f"Описание: {self.description}"
        )
