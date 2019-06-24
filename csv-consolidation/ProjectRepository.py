import sqlite3


class ProjectRepository:
    def __init__(self, connection: sqlite3.Connection, title: str, manager: str, deadline: int):
        # TODO: перенести title: str, manager: str, deadline: int в метод store
        """
        Хранилище атрибутов проекта

        :param connection: соединение с СУБД
        :param title: Наименование проекта
        :param manager: ФИО руководителя
        :param deadline: Дата сдачи
        """
        self.connection = connection
        self.title = title
        self.manager = manager
        self.deadline = deadline

    def store(self) -> bool:
        """
        Сохранить (записать в хранилище) атрибуты проекта

        Дубли (по наименованию) не будут записаны

        :return: результат записи атрибутов
        """
        cursor = self.connection.cursor()

        write_project = "INSERT INTO project SELECT NULL,?,?,? WHERE NOT EXISTS (" \
                        "SELECT NULL FROM project WHERE title=?)"
        cursor.execute(write_project, (self.title, self.manager, self.deadline, self.title))
        is_success = cursor.rowcount > 0
        self.connection.commit()

        return is_success
