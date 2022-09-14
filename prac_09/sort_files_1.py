
import os
import shutil


FILE_DESTINATION = "FilesToSort"


def main():
    """Movie files with same extension to the the same directory."""
    os.chdir(FILE_DESTINATION)
    print(f"Sorting files in: {FILE_DESTINATION}")
    for directory_name, subdirectory, filename in os.walk('.'):
        type_list = create_type_list(filename)

        for ext_type in type_list:
            try:
                os.mkdir(ext_type)
            except FileExistsError:
                pass
        try:
            for file in filename:
                file_ext = get_extension(file)
                shutil.move(file, file_ext)
        except shutil.Error:
            pass
    print("Sort complete")



def create_type_list(filenames):
    """Create a list of the different types of extensions in the target file."""
    type_list = []
    for file in filenames:
        file_ext = get_extension(file).replace('.', '')
        if file_ext not in type_list:
            type_list.append(file_ext)
    return type_list


def get_extension(file):
    """Get the extension of target file."""
    file_type = file.split('.')[-1]
    return file_type





main()