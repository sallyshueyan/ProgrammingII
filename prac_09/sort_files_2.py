
import os


def main():
    """Move files into where user wants to store them."""
    ext_type_to_cat = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        ext = get_extension(filename)
        if ext not in ext_type_to_cat:
            category = input("What category would you like to sort {} files into? ".format(ext))
            ext_type_to_cat[ext] = category


        os.rename(filename, "{}/{}".format(ext_type_to_cat[ext], filename))

def get_extension(filename):
    """Get the extension of target file."""
    ext = filename.split('.')[-1]
    return ext



main()