import random
from DataCrawler import DataCrawler
from ProjectHeader import ProjectHeader
from Contributor import Contributor


class DataGenerator:
    TIME_OVER = 1666666666
    TIME_BEGINING = 100500

    def __init__(self, crawler):
        """

        :type crawler: DataCrawler
        """
        self.crawler = crawler

    def load_data(self):
        self.crawler.obtain_data()

    def get_projects(self, volume=2):
        crawler = self.crawler
        projects = []
        for i in range(volume):
            title = f"{crawler.get_some_variety()} {crawler.get_some_name()}"
            manager = f"{crawler.get_some_variety()}"
            deadline = random.choice(range(self.TIME_BEGINING, self.TIME_OVER))

            project = ProjectHeader(title, manager, deadline)
            projects.append(project)

        return projects

    def get_collaboration(self, volume=2, repeatability=2):
        crawler = self.crawler

        collaboration = []
        for i in range(volume):
            employee = f"{crawler.get_some_variety()}"

            for ii in range(random.choice(range(1, repeatability))):
                pie = random.choice(range(0, 4))
                contributor = Contributor(employee, pie)
                collaboration.append(contributor)

        return collaboration


# attempt
