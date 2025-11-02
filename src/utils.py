from src.vacancy import Vacancy


def vacancies_by_name(vacancies: list):
    """Функция вывода вакансий с hh.ru"""
    try:
        if not vacancies:
            print("Вакансии не найдены.")
        else:
            for vac in vacancies:
                vacancy_obj = Vacancy(name=vac.get('name', 'Нет названия'),
                                      link=vac.get('alternate_url', 'Нет ссылки'),
                                      salary=vac.get("salary"),
                                      description=vac.get("snippet", {}).get("requirement", "Нет описания"))
                print(vacancy_obj)

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    pass


def top_vacancies(vacancies: list[Vacancy], top=10):
    return sorted(vacancies, reverse=True)[:top]


if __name__ == "__main__":
    print("Hi")
