words = {}

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_name = filedialog.askopenfilename(initialdir="./", title="Select file",
                                       filetypes=(("all files", "*.*"), ("jpeg files", "*.jpg")))
if file_name == None or file_name == "":
    print("No File selected")
    exit(0)

with open(file_name, 'r') as f:
    line = f.readline()
    while line != "":
        for word in line.split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

        line = f.readline()

with open('output.txt', 'w') as f:
    for key, value in words.items():
        f.write(key + ": " + str(value) + "\n")
        print(key + ": " + str(value) + "\n")