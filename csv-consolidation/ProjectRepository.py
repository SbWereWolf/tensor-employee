import sqlite3


class ProjectRepository:
    def __init__(self, connection: sqlite3.Connection, title: str, manager: str, deadline: int):
        self.connection = connection
        self.title = title
        self.manager = manager
        self.deadline = deadline

    def store(self):
        cursor = self.connection.cursor()

        write_project = "INSERT INTO project SELECT NULL,?,?,? WHERE NOT EXISTS (" \
                        "SELECT NULL FROM project WHERE title=?)"
        cursor.execute(write_project, (self.title, self.manager, self.deadline, self.title))
        is_success = cursor.rowcount > 0
        self.connection.commit()

        return is_success
