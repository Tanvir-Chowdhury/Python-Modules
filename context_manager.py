import os
from contextlib import contextmanager

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

