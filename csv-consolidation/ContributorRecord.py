import sqlite3


class ContributorRecord:
    def __init__(self, connection: sqlite3.Connection, name: str, value: str):
        self.connection = connection
        self.name = name
        self.value = value

    def store(self, project: str):
        cursor = self.connection.cursor()

        write_contributor = "INSERT INTO contributor " \
                            "SELECT NULL,(select id from project where title = ? ),?,? WHERE NOT EXISTS (" \
                            "SELECT NULL FROM contributor WHERE name=? " \
                            "and project_id = (select id from project where title = ? ))"
        cursor.execute(write_contributor, (project, self.name, self.value, self.name, project))
        is_success = cursor.rowcount > 0
        self.connection.commit()

        return is_success
