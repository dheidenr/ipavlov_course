import tempfile
import os


class File:
    """This object is intended for reading a file."""

    def __init__(self, path_file):
        self.path_file = path_file
        if not os.path.exists(path_file):
            open(self.path_file, mode='w').close()
        self.file_lines = self.read().split('\n')
        if len(self.file_lines) > 0:
            del self.file_lines[-1]
        self.index_iter = 0

    def read(self):
        try:
            with open(self.path_file, mode='r') as file:
                return file.read()
        except FileNotFoundError:
            return ''

    def write(self, line: str):
        try:
            with open(self.path_file, mode='w') as file:
                return file.write(line)
        except FileNotFoundError:
            return 0

    def __str__(self):
        return os.path.join(tempfile.gettempdir(), self.path_file)

    def __add__(self, other):
        if not isinstance(other, File):
            raise ValueError
        line_self = self.read() if os.path.exists(self.path_file) else ''
        line_other = other.read() if os.path.exists(other.path_file) else ''
        result = File(os.path.join(
            tempfile.gettempdir(),
            os.path.splitext(os.path.basename(self.path_file))[0]
            + '_Add_' +
            os.path.splitext(os.path.basename(other.path_file))[0]
        ))
        result.write(line_self + line_other)
        return result

    def __iter__(self):
        return self

    def __next__(self):
        # print(len(self.file_lines))
        # print(self.index_iter)
        if 0 < len(self.file_lines) and self.index_iter < len(self.file_lines):
            result = self.file_lines[self.index_iter]
            # print(f'result: {result}, index_iter:{self.index_iter}')
            # print(self.file_lines[self.index_iter])
        else:
            raise StopIteration
        self.index_iter += 1
        # print(f'index_iter: {self.index_iter}')
        return result


# if __name__ == '__main__':
#     print(tempfile.gettempdir())
#     print(os.path.join(tempfile.gettempdir(), r'test.txt'))
#     file1 = File('file1.txt')
#     file1.write('file1_str1\nfile1_str2\nfile1_str3')
#     file2 = File('file2.txt')
#     file2.write('file2_str1\nfile2_str2\nfile2_str3')
#     file3 = file1 + file2
#     print(f'{file1}, {file2}, {file3}')
#
#     print('*' * 50 + '--print file 3--' + '*' * 50)
#     for i in file3:
#         print(i)
#
#     # print(file3.index_iter)
#     # print(file3.__next__())
