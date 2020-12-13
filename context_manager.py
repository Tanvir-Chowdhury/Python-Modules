import os
from contextlib import contextmanager

class Context_Manager():
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()

@contextmanager
def change_dir(destination):
    cwd = os.getcwd()
    os.chdir(destination)
    print(os.listdir())
    yield
    os.chdir(cwd)

