import random
import sqlite3
from CollaborationStorage import CollaborationStorage


class CollaborationHandler:
    def __init__(self, data, connection: sqlite3.Connection):
        self.data = data
        self.connection = connection

    def store_collaboration(self, project_identifier):
        for i in range(1, random.choice(range(1, 6))):
            contributor = random.choice(self.data)
            storage = CollaborationStorage(project_identifier, contributor, self.connection)
            storage.store_data()
