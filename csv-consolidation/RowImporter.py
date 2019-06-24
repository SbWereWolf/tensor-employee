import datetime
import sqlite3
import time

from ContributorRecord import ContributorRecord
from ProjectRepository import ProjectRepository


class RowImporter:
    def __init__(self, connection: sqlite3.Connection, header: [str]):
        """
        Импортёр информации из строки с данными

        :param connection: соединение с СУБД
        :param header: заголовки колонок с количеством работы участников проекта
        """
        self.connection = connection
        self.header = header

    def run(self, row: [str]) -> bool:
        """
        Разобрать данные и записать информацию в БД

        :param row: данные
        :return: результат записи информации с атрибутами проекта
        """
        title = row[0]
        manager = row[1]
        deadline = int(time.mktime(datetime.datetime.strptime(row[2], "%d.%m.%Y").timetuple()))

        project = ProjectRepository(self.connection, title, manager, deadline)
        is_success = project.store()

        if is_success:
            i = 1
            for contributor in self.header:
                value = row[2 + i]
                is_empty = len(value) == 0
                if not is_empty:
                    record = ContributorRecord(self.connection, contributor, value)
                    record.store(title)
                i = i + 1

        return is_success
