#!/usr/bin/python3
def read_file(filename=""):
    with open("my_file_0.txt", encoding="utf-8") as my_file:
        file = my_file.read()
        print(file)
