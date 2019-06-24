import sqlite3


class ContributorRecord:
    def __init__(self, connection: sqlite3.Connection, name: str, value: str):
        # TODO: перенести name: str, value: str в метод store
        """
        Обработчик записи об участники проекта

        :param connection: соединение с СУБД
        :param name: ФИО участника
        :param value: количество работы (участия)
        """
        self.connection = connection
        self.name = name
        self.value = value

    def store(self, project: str) -> bool:
        """
        Сохранить (записать) информацию об участнике проекта

        :param project: наименование проекта (уникальный идентификатор проекта)
        :return: результат записи
        """
        cursor = self.connection.cursor()

        write_contributor = "INSERT INTO contributor " \
                            "SELECT NULL,(select id from project where title = ? ),?,? WHERE NOT EXISTS (" \
                            "SELECT NULL FROM contributor WHERE name=? " \
                            "and project_id = (select id from project where title = ? ))"
        cursor.execute(write_contributor, (project, self.name, self.value, self.name, project))
        is_success = cursor.rowcount > 0
        self.connection.commit()

        return is_success
