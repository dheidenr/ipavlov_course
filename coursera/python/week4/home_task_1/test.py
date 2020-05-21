import os.path
from coursera.python.week4.home_task_1.solution import File
path_to_file = r'C:\Users\kurator\PycharmProjects\ipavlov_course\coursera\python\week4\home_task_1\some_filename'
print(os.path.exists(path_to_file))
# False
file_obj = File(path_to_file)
print(os.path.exists(path_to_file))
# True
print(file_obj.read())
# ''
print(file_obj.write('some text'))
# 9
print(file_obj.read())
# 'some text'
print(file_obj.write('other text'))
# 10
print(file_obj.read())
# 'other text'
file_obj_1 = File(path_to_file + '_1')
file_obj_2 = File(path_to_file + '_2')
print(file_obj_1.write('line 1\n'))
# 7
print(file_obj_2.write('line 2\n'))
# 7
new_file_obj = file_obj_1 + file_obj_2
print(isinstance(new_file_obj, File))
# True
print(new_file_obj)
# C:\Users\Media\AppData\Local\Temp\71b9e7b695f64d85a7488f07f2bc051c
for line in new_file_obj:
    print(ascii(line))
# 'line 1\n'
# 'line 2\n'
