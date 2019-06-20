from pathlib import Path


class FileCrawler:
    def __init__(self, filemask: str):
        """

        :type filemask: str
        """
        self.filemask = filemask

    def gather_names(self):
        files = list(Path('.').glob(self.filemask))
        names = []
        for file in files:
            names.append(file.name)

        return names
