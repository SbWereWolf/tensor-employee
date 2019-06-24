class DataAdjuster:
    def __init__(self, names, report_data):
        """
        Фоматировщик данных отчёта для записи в CSV

        :param names: ФИО участников проекта
        :param report_data: данные об участии
        """
        self.report_data = report_data
        self.names = names

    def run(self) -> [tuple]:
        """
        Отформатировать данные отчёта для записи в CSV

        :return: список кортежей с данными отчёта
        """
        header = ('project', 'manager', 'deadline')

        for name in self.names:
            header = header + (name,)

        output_data = [header] + self.report_data

        return output_data
