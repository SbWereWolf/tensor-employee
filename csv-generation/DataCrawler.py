import random


class DataCrawler:
    READ_ONLY = "r"
    names_source = 'noun.txt'
    varieties_source = 'adjective.txt'

    names = []
    varieties = []

    def __init__(self, names_path, varieties_path, capacity=100, employee_limit=3):
        self.capacity = capacity
        self.employee_limit = employee_limit
        self.names_source = names_path
        self.varieties_source = varieties_path

    @staticmethod
    def trim_eol_symbol(raw_elements):
        pure_elements = []
        for element in raw_elements:
            pure = element.rstrip("\n")
            pure_elements.append(pure)

        return pure_elements

    def read_file(self, filename):
        with open(filename, self.READ_ONLY) as handle:
            lines = handle.readlines()
            handle.close()

        rows = self.trim_eol_symbol(lines)

        return rows

    def obtain_data(self):
        self.names = self.read_file(self.names_source)
        self.varieties = self.read_file(self.varieties_source)

    def get_some_name(self):
        result = random.choice(self.names)

        return result

    def get_some_variety(self):
        result = random.choice(self.varieties)

        return result
