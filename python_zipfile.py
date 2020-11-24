from zipfile import ZipFile
import os

def get_all_file_paths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory): 
        directories = directories
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths

def main():
    filepaths = get_all_file_paths("/home/codinxter/Downloads/")
    print("following files will be ziped")
    for filenames in filepaths:
        print(filenames)

    with ZipFile("my_python_zip.zip", "w") as zip:
        for filenames in filepaths:
            zip.write(filenames)
    
if __name__ == "__main__":
    main()



'''from zipfile import ZipFile

with Zipfile("my_python_zip.zip", "r") as zip:
    zip.printdir()
    zip.extractall(filenames)
'''