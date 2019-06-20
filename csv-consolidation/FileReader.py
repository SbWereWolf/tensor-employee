import csv


class FileReader:
    def __init__(self, files: [str]):
        self.files = files

    def run(self):
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
