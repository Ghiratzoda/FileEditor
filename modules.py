import pathlib
from datetime import datetime
import os
CWD = pathlib.Path.cwd()
class FileEditor:

    """
    This is a experimental class which can:
    1) creating file
    2) creating folder
    3) delete dir
    4) delete file
    5) dir info (What is in the file)
    6) rename (file/folder etc.)
    7) reading and edditing fie
    and etc..
    """
    # def __init__(self):
    #This module creates file in cwd if it does not exist
    # 2 Task from project
    def create_file():
        newfile = input("Enter a filename and filetype (main.py)")
        new_file = CWD / newfile
        if not new_file.exists():
            print(f"File {newfile} successfully created!")
            new_file.touch()
        else:
            print(f"{newfile} exists in this folder. Try another name")

    #This module creates directory in cwd if it does not exist
    # 3 Task from project
    def create_dir():
        newdir = input("Enter a directory name")
        new_dir = CWD / newdir
        if not new_dir.exists():
            print(f"Folder {newdir} successfully created!")
            new_dir.mkdir(parents=True)
        else:
            print(f"{newdir} directory exists in this folder. Try another name")

    # This module deletes an item
    def delete_file():
        newfile = input("Enter a filename and filetype (main.py)")
        new_file = CWD / newfile
        new_file.unlink()

    #This module creates directory in cwd if it does not exist
    # 4 Task from project
    def delete_dir():
        newdir = input("Enter a directory name")
        new_dir = CWD / newdir
        try:
            new_dir.rmdir()
        except OSError:
            query = input("folder has items inside. Do you want tp delete them all Yes[y], Np[n]")
            if query == 'y':
                for items in new_dir.iterdir():
                    items.rmdir()
                else:
                    return "Folder has not been deleted"
        print("succesfully deleted")


    def convert_date(timestamp):
        d = datetime.utcfromtimestamp(timestamp)
        formatted_date = d.strftime('%d %b %Y')
        return formatted_date

    # 1 Task from project
    def dir_info():
        for entry in CWD.iterdir():
            if entry.is_file():
                info = entry.stat()
                print(f'Name: {entry.name}\t Last Modified: {convert_date(info.st_mtime)} \t Size : {os.stat(entry).st_size} kb')

    def rename():
        old_name = input("What item (file/folder, etc.) do you want to rename?")
        new_name = input("Enter the new name for the item: ")
        try:
            pathlib.Path.rename(old_name, new_name)
            print(f"{old_name} renamed to {new_name} successfully!")
        except FileNotFoundError:
            print(f"{old_name} does not exist in this folder.")

    def read_file(filename, mode):
        path = CWD / filename
        if mode == 'r':
            with open (path, mode) as file:
                text = file.read()
                print(text)
        elif mode == 'a':
            with open (path, mode) as file:
                text = file.write("\n"+input(f"Enter your idea here to add on {filename} file: "))
                print(text)
    
    def search_in_folder(searching_item):
        print("This module is not prepared yet. \nSorry We are working on it")
    
    def move_cwd():
        print("To go forword dir use ( / foldername). To go to backdir just write --")
        print("This module is not prepared yet. \nSorry We are working on it")
