from setuptools import setup, find_packages

setup(
    name="VolkhinPythonLearnig",
    version="1",
    packages=find_packages(),
    scripts=['run_consolidation.py',
             'ContributorRecord.py',
             'DataAdjuster.py',
             'DataParser.py',
             'FileCrawler.py',
             'FileReader.py',
             'ProjectRepository.py',
             'projects.sqlite',
             'ReportExtractor.py',
             'RowImporter.py',
             'output/.gitkeep'
             ],

    package_data={
        '': ['*.sql', '*.sqlite', '*.md'],
    },

    # metadata to display on PyPI
    author="Volkhin Nikolay",
    author_email="ulfnew@gmail.com",
    description="Tensor test task solution for Python developer",
    keywords="Tensor Python test",
    url="https://github.com/SbWereWolf/tensor-employee/blob/master/csv-consolidation/",
    project_urls={
        "Author Github Profile": "https://github.com/SbWereWolf",
        "Documentation": "https://github.com/SbWereWolf/tensor-employee/blob/master/csv-consolidation/README.md",
        "Source Code": "https://github.com/SbWereWolf/tensor-employee/blob/master/csv-consolidation/",
    },
    classifiers=[
        'License :: copyleft'
    ]
)
