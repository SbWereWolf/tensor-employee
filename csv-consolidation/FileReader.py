import csv


class FileReader:
    def __init__(self, files: [str]):
        """
        Вычитыватель файлов

        :param files: список файлов для считывания
        """
        self.files = files

    def run(self) -> [list]:
        """
        Считать содержимое файлов

        :return: список со строками, строки будут сгруппированны по файлам источникам
        """
        content = []
        for file in self.files:
            raws = list(csv.reader(open(file, "r")))
            rows = []
            for line in raws:
                is_empty = len(line) == 0
                if not is_empty:
                    rows.append(line)
            content.append(rows)

        return content
