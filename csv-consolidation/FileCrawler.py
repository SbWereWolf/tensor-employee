from pathlib import Path


class FileCrawler:
    def __init__(self, filemask: str):
        """
        Сборщика имён файлов

        :param filemask: маска для отбора файлов
        """
        self.filemask = filemask

    def gather_names(self) -> [str]:
        """
        Собрать имена файлов

        :return: список с именами файлов
        """
        files = list(Path('.').glob(self.filemask))
        names = []
        for file in files:
            names.append(file.name)

        return names
