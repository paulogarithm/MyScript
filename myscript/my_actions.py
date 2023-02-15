import os

from my_color import *

this_dir = os.path.dirname(os.path.realpath(__file__)) + "/.."

def its_a_file(my_file: str):
    NAME = input("Enter the link name - ")
    if os.path.isfile(f"{this_dir}/links/{NAME}"):
        print(f"{my_color.red}Name already in use.\n{my_color.default}")
        return its_a_file(my_file)

    os.system(f"mv {my_file} {this_dir}/source")
    os.system(f"chmod +x {this_dir}/source/{my_file}")
    os.system(f"ln -s {this_dir}/source/{my_file} {this_dir}/links/{NAME}")
    print(f"{my_color.green}Successfully added{my_color.default}")


def its_a_folder(my_folder: str, name=None):
    NAME = input("Enter the link name - ") if not name else name
    if os.path.isfile(f"{this_dir}/links/{NAME}"):
        print(f"{my_color.red}Name already in use.\n{my_color.default}")
        return its_a_file(my_folder)

    BIN = input("Enter binary name - ")
    if not BIN in os.listdir(my_folder):
        print(f"{my_color.red}Binary not in folder.\n{my_color.default}")
        return its_a_folder(my_folder, NAME)

    os.system(f"mv {my_folder} {this_dir}/source")
    os.system(f"chmod +x {this_dir}/source/{my_folder}/{BIN}")
    os.system(f"ln -s {this_dir}/source/{my_folder}/{BIN} {this_dir}/links/{NAME}")

    print(f"{my_color.green}Successfully added{my_color.default}")


def remove(arg: str):
    if not arg in os.listdir(f"{this_dir}/links"):
        print(f"{my_color.red}This command does not exist.{my_color.default}")
        exit(69)
    while True:
        response = input(f"Delete '{arg}' permanently ? [y/N] ")
        if response.lower() == "y" or response.lower() == "yes":
            REAL_PATH = os.path.dirname(os.path.realpath(f"{this_dir}/links/{arg}"))
            os.system(f"rm -rf {REAL_PATH}")
            os.remove(f"{this_dir}/links/{arg}")
            print(f"'{arg}' has been successfully deleted.")
            break
        elif response.lower() == "n" or response.lower() == "no" or response == "":
            break
