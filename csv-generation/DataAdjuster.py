class DataAdjuster:
    def __init__(self, names, report_data):
        self.report_data = report_data
        self.names = names

    def run(self):
        header = ('project', 'manager', 'deadline')

        for name in self.names:
            header = header + (name,)

        output_data = [header] + self.report_data

        return output_data
