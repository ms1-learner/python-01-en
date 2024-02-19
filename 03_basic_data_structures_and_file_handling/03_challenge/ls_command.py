import os


def ls_command(directory):
    # If a user's input is "sample", directory will be "sample".
    # You don't have to think about the invalid directory path!

    # Remove "pass" and write your code here.
    pass


if __name__ == "__main__":
    directory_path = input("Enter directory path to organize files: ")

    if not os.path.isdir(directory_path):
        print("Invalid directory path.")
    else:
        ls_command(directory_path)
