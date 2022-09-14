import os


def find_in_files(search_string, file_extension, files_found):
    """Find files of type file_extension that contain search_string."""
    count = 0
    for directory_name, directories, filenames in os.walk("."):
        for filename in filenames:
            if os.path.splitext(filename)[1] == file_extension:
                count += 1
                current_file = open(os.path.join(directory_name, filename), 'r')
                text = current_file.read()
                if search_string in text:
                    full_filename = os.path.join(directory_name, filename)
                    files_found.append(full_filename)
                current_file.close()
    return count


def test_find():
    filenames = []
    search_string = "print"
    file_extension = ".py"
    count = find_in_files(search_string, file_extension, filenames)
    print("Examined {} {} files and found '{}' in:\n{}".format(count, file_extension, search_string, filenames))


test_find()
