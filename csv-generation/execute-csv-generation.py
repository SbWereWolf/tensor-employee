import sqlite3
import csv
from DataCrawler import DataCrawler
from DataGenerator import DataGenerator
from ProjectStorage import ProjectStorage
from CollaborationHandler import CollaborationHandler
from ReportExtractor import ReportExtractor
from DataAdjuster import DataAdjuster

NOUN = 'noun.txt'
ADJECTIVE = 'adjective.txt'

generator = DataGenerator(DataCrawler(NOUN, ADJECTIVE))
generator.load_data()
projects = generator.get_projects(10)
collaboration = generator.get_collaboration(5, 20)

connection = sqlite3.connect("projects.sqlite")

storage = ProjectStorage(connection)
identifiers = storage.store_data(projects)
for project_identifier in identifiers:
    (CollaborationHandler(collaboration, connection)).store_collaboration(project_identifier[0])

extractor = ReportExtractor(connection)
names = extractor.extract_names()
report_data = extractor.get_data(names)

adjuster = DataAdjuster(names, report_data)
output_data = adjuster.run()

with open('projects.csv', 'w') as out:
    csv_out = csv.writer(out)
    csv_out.writerows(output_data)

pass
