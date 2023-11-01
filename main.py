from modules import FileEditor
from modules import FileManagment


text = """
1) creating file
2) creating folder
3) delete dir
4) delete file
5) dir info (What is in the file)
6) rename (file/folder etc.)
7) reading and edditing fie
8) search for something
9) move swd
10) Creating a new file by OOP

"""
run = True
while run:
    def start_point():
        print(text)
        operator = int(input("What's on your mind? "))
        if operator == 1:
            FileEditor.create_file()
        elif operator == 2:
            FileEditor.create_dir()
        elif operator == 3:
            FileEditor.delete_dir()
        elif operator == 4:
            FileEditor.delete_file()
        elif operator == 5:
            FileEditor.dir_info()
        elif operator == 6:
            FileEditor.rename()
        elif operator == 7:
            FileEditor.read_file(input("filename (data.txt)"), input("read[r], add[a]"))
        elif operator == 8:
            FileEditor.search_in_folder()
        elif operator == 9:
            FileEditor.move_cwd()
        elif operator == 0:
            run = False
        elif operator == 10:
            file_obj = FileManagment('Peter.txt')
            print(file_obj)
        else:
            print("None operation was choosed, please try again!")
            start_point()
    start_point()