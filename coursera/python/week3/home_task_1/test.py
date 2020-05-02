
from coursera.python.week3.home_task_1.solution import FileReader

import sys

reader = FileReader('not_exist_file.txt')
text = reader.read()
print("No text:", text)

with open('some_file.txt', 'w') as file:
    file.write('some text')
reader = FileReader('some_file.txt')
text = reader.read()
print("Yes text:", text)
print("type", type(reader))

