# Вспомонательные скрипты для генерации тестовых данных

Тестовые данные это информация о проектах и степени участия отдельных сотрудников в работе по этим проектам

Тестовые данных выдаются в формате CSV файла

## Назначение файлов

 - adjective.txt словарь прилагательных
 - noun.txt словарь существительных
 - projects.sqlite файл базы данных
 - database-for-csv-generation.sql скрипт для разворачивания структуры базы данных
 - execute-csv-generation.py собственно скрипт для генерации данных
 - projects.csv выходной файл работы скрипта (меняем магические числа в скрипте и получаем разное количество колонок в CSV)
 
 ## Инструкция по эксплуатации
 
 - скопировать директорию tensor-employee\csv-generation (файл projects.csv можно проигнорировать)
 - установить Python 3.7.3 и SQLite 3.25.1
 - выполнить скрипт database-for-csv-generation.sql

 ## Руководство пользователя
 
 В скрипте execute-csv-generation.py магические числа в строках:
 ```
projects = generator.get_projects(10)
collaboration = generator.get_collaboration(5, 20) 
 ``` 
 определяют количество проектов (10), возможное максимальное количество участников (5), возможное максимальное количество повторений участника (20)
 
 Скрипт сгенерит два списка:
 - список проектов
 - список участников, где уникальных будет не более заданного количества, и каждый из уникальных участников может встречаться в списке не более указанного количества раз
 
 Для каждого проекта случайным образом будут выбраны участники и им будет назначено от 0 до 4 долей участия в работе над проектом
 
 Одновременно с генерацией списков происходит запись в БД (уникальность контролируется на стороне БД)
 
 Из БД будет сделана выгрузкав в файл projects.csv
 
 Поскольку каждый раз выполняется выгрузка из БД, то при каждом запуске скрипта таблицы необходимо очищать:
 ```
 DELETE
FROM collaboration
WHERE 1 = 1;
DELETE
FROM raw_project
WHERE 1 = 1;
 ```
 
 Скрипты были написаны для себя, с качеством "лишь бы работало", качество не надо принимать за образцовое :)
