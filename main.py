from src.hh_api import HHApi
from src.utils import top_vacancies, vacancies_by_name
from src.vacancy import Vacancy

hh = HHApi()


def integer_input(word_inp):  # pragma no cover
    """
    Вспомогательная функция для запроса топа вакансий по ЗП.
    Определяет положительность запроса.
    """
    while True:
        try:
            value = int(input(word_inp))
            if value <= 0:
                print("Пожалуйста, введите положительное число.")
                continue
            return value
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")


def main():
    """Основная функция взаимодействия с пользователем"""
    print("Добро пожаловать!")
    while True:
        print("1. Поиск вакансий по ключевому слову на hh.ru")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Найти вакансии с ключевым словом в описании")
        num_op = input("Введите номер опции: ").strip()
        if num_op == '1':
            try:
                word_int = input("Введите поисковый запрос для поиска вакансий: ").strip()
                vacancies = hh.get_vacancies(word_int)
                vacancies_by_name(vacancies)
                break
            except Exception as e:
                print(f"Произошла ошибка: {e}")
        elif num_op == '2':
            top = integer_input("Введите количество топ вакансий по зарплате: ")
            word_int = input("Введите поисковый запрос для фильтрации (оставьте пустым для всех): ").strip()
            try:
                vacancies = hh.get_vacancies(word_int)
                list_vacancy = []
                # Создаем список объектов Vacancy
                for vac in vacancies:
                    vacancy_obj = Vacancy(name=vac.get('name', 'Нет названия'),
                                          link=vac.get('alternate_url', 'Нет ссылки'),
                                          salary=vac.get("salary"),
                                          description=vac.get("snippet", {}).get("requirement", "Нет описания"))
                    list_vacancy.append(vacancy_obj)
                top_vac = top_vacancies(list_vacancy, top)
                for vac in top_vac:
                    print(vac)
                break
            except Exception as e:
                print(f"Произошла ошибка: {e}")
                break
        elif num_op == '3':
            keyword_in_desc = input("Введите ключевое слово для поиска в описании вакансии: ").strip().lower()
            print("-" * 100)  # для отделения ввода и вывода
            try:
                vacancies = hh.get_vacancies("")
                list_vacancy = []
                for vac in vacancies:
                    description = vac.get("snippet", {}).get("requirement")
                    if description and keyword_in_desc in description:
                        vacancy_obj = Vacancy(name=vac.get('name', 'Нет названия'),
                                              link=vac.get('alternate_url', 'Нет ссылки'),
                                              salary=vac.get("salary"),
                                              description=vac.get("snippet", {}).get("requirement", "Нет описания"))
                        list_vacancy.append(vacancy_obj)
                if not list_vacancy:
                    print("Вакансии с указанным ключевым словом в описании не найдены.")
                    break
                else:
                    for vac in list_vacancy:
                        print(vac)
                    break
            except Exception as e:
                print(f"Произошла ошибка: {e}")
                break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
