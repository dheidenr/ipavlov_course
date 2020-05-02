

class FileReader:
    """This object is intended for reading a file."""
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        try:
            with open(self.filename, mode='r') as file:
                return file.read()
        except FileNotFoundError:
            return ''
