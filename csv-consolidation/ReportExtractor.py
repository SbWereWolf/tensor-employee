import sqlite3


class ReportExtractor:
    def __init__(self, connection: sqlite3.Connection):
        """
        Формирователь данных для отчёта

        :param connection: соединение с СУБД
        """
        self.connection = connection

    def extract_names(self) -> [str]:
        """
        Получить ФИО участников всех проектов

        Сорудники без участия в проектах будут проигнорированы

        :return:  список ФИО участников
        """
        get_contributors = "select name from contributor where value >0 and value IS NOT NULL group by name"

        cursor = self.connection.cursor()
        cursor.execute(get_contributors)
        contributors = cursor.fetchall()

        names = []
        for contributor in contributors:
            names.append(contributor[0])

        return names

    def get_data(self, names: [str]) -> [tuple]:
        """
        Сформировать данные для отчёта

        Сорудники без участия в проектах будут проигнорированы

        :param names: ФИО участников для отчёта
        :return: информация об участии сотрудников в проектах
        """
        names_part = ''
        number = 0
        COMMA = ','
        for name in names:
            number = number + 1
            names_part = f"{names_part}" \
                f"(select value from contributor " \
                f"where project_id = p.id " \
                f"and name = '{name}' " \
                f"and value >0 " \
                f"and value IS NOT NULL) AS a{number}{COMMA}"

        names_part = names_part.rstrip(COMMA)
        data_request = f"select title,manager,strftime('%d.%m.%Y', deadline, 'unixepoch'),{names_part} " \
            f"from project p " \
            f"ORDER BY deadline"

        cursor = self.connection.cursor()
        cursor.execute(data_request)
        report_data = cursor.fetchall()

        return report_data
