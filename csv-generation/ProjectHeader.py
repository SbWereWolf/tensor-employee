import datetime


class ProjectHeader:

    def __init__(self, title="", manager="", deadline=datetime.date(1, 1, 1)):
        self.title = title
        self.manager = manager
        self.deadline = deadline
