import sqlite3


class ReportExtractor:
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection

    def extract_names(self):
        get_contributors = "select contributor from collaboration group by contributor"

        cursor = self.connection.cursor()
        cursor.execute(get_contributors)
        contributors = cursor.fetchall()

        names = []
        for contributor in contributors:
            names.append(contributor[0])

        return names

    def get_data(self, names):
        names_part = ''
        number = 0
        for name in names:
            number = number + 1
            names_part = f"{names_part}" \
                f"(select pie from collaboration where raw_project_id = id and contributor = '{name}') AS a{number},"

        names_part = names_part.rstrip(',')
        data_request = f"select title,manager,strftime('%d.%m.%Y', deadline, 'unixepoch'),{names_part} from raw_project"

        cursor = self.connection.cursor()
        cursor.execute(data_request)
        report_data = cursor.fetchall()

        return report_data
