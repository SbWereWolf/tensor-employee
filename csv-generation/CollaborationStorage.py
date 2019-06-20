import sqlite3
from Contributor import Contributor


class CollaborationStorage:
    contributor: Contributor

    def __init__(self, identifier, contributor, connection: sqlite3.Connection):
        self.identifier = identifier
        self.contributor = contributor
        self.connection = connection

    def store_data(self):
        contributor = self.contributor
        data = (self.identifier, contributor.contributor, contributor.pie, self.identifier, contributor.contributor)
        cursor = self.connection.cursor()

        write_contributor = "INSERT INTO collaboration SELECT ?,?,? WHERE NOT EXISTS (" \
                            "SELECT NULL FROM collaboration c WHERE c.raw_project_id=? AND c.contributor=?)"
        cursor.execute(write_contributor, data)
        self.connection.commit()
