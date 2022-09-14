
import os


def main():
    """Move files into where user wants to store them."""
    ext_type_to_cat = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue


main()