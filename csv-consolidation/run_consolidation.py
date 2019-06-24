import csv
import sqlite3

from DataAdjuster import DataAdjuster
from DataParser import DataParser
from FileCrawler import FileCrawler
from FileReader import FileReader
from ReportExtractor import ReportExtractor

print(" please be aware of DISCLAIMER : No error handling , No data validation ")

filenames = FileCrawler("*.csv").gather_names()
data = FileReader(filenames).run()

connection = sqlite3.connect("projects.sqlite")

parser = DataParser(data, connection)
parser.parse()

extractor = ReportExtractor(connection)
names = extractor.extract_names()
report_data = extractor.get_data(names)

adjuster = DataAdjuster(names, report_data)
output_data = adjuster.run()

# TODO: убрать в отдельный класс
# Записываем в выходной файл консолидированные данные по участию в проектах
with open('output/report.csv', 'w') as out:
    csv_out = csv.writer(out)
    csv_out.writerows(output_data)

print(" Data place into output/report.csv")
