import sqlite3
from .ProjectHeader import ProjectHeader


class ProjectStorage:
    projects = []

    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection

    @staticmethod
    def prepare_data(data):
        projects = []
        project: ProjectHeader
        for project in data:
            projects.append((project.title, project.manager, project.deadline, project.title))

        return projects

    def store_data(self, data):
        projects = self.prepare_data(data)

        cursor = self.connection.cursor()

        write_projects = "INSERT INTO raw_project SELECT NULL,?,?,? WHERE NOT EXISTS (" \
                         "SELECT NULL FROM raw_project  WHERE title=?)"
        cursor.executemany(write_projects, projects)
        self.connection.commit()

        get_identifiers = "SELECT id FROM raw_project ORDER BY id"
        cursor.execute(get_identifiers)
        result = cursor.fetchall()

        return result
