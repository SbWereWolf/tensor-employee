import sqlite3

from RowImporter import RowImporter


class DataParser:
    def __init__(self, data, connection: sqlite3.Connection):
        self.connection = connection
        self.data = data

    def parse(self):
        for content in self.data:
            is_header = True
            for row in content:
                if not is_header:
                    importer.run(row)

                if is_header:
                    is_header = False

                    header = row[slice(-1, 2 - len(row), -1)]
                    importer = RowImporter(self.connection, header)
                pass
