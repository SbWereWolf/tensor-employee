import datetime
import sqlite3
import time

from ContributorRecord import ContributorRecord
from ProjectRepository import ProjectRepository


class RowImporter:
    def __init__(self, connection: sqlite3.Connection, header: [str]):
        self.connection = connection
        self.header = header

    def run(self, row: [str]):
        title = row[0]
        manager = row[1]
        deadline = int(time.mktime(datetime.datetime.strptime(row[2], "%d.%m.%Y").timetuple()))

        project = ProjectRepository(self.connection, title, manager, deadline)
        is_success = project.store()

        if is_success:
            i = 0
            for contributor in self.header:
                value = row[3 + i]
                is_empty = len(value) == 0
                if not is_empty:
                    record = ContributorRecord(self.connection, contributor, value)
                    record.store(title)
                i = i + 1

        return is_success
