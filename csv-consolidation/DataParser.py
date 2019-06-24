import sqlite3

from RowImporter import RowImporter


class DataParser:
    def __init__(self, data, connection: sqlite3.Connection):
        """
        Парсер для данных о проектах

        :param data: CSV строки сгруппированные по файлам источникам
        :param connection: соединение с СУБД для записи информации
        """
        self.connection = connection
        self.data = data

    def parse(self):
        """
        Разобрать данные
        """
        for content in self.data:
            is_header = True
            # TODO: использовать генератор для обработки строк
            for row in content:
                if not is_header:
                    importer.run(row)

                if is_header:
                    is_header = False

                    header = row[slice(-1, 2 - len(row), -1)]
                    importer = RowImporter(self.connection, header)
                pass
