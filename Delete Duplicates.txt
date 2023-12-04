#______________________________________________________________
#   Author:         Jaden Dzubiel
#   Date Created:   2023/12/04
#   Description:    Delete duplicate files
#______________________________________________________________

from tkinter import *
from tkinter import filedialog
from pathlib import Path
import os
import tkinter as tk
import tkinter.messagebox
import fnmatch

#   FIRST GUI MAIN MENU

class Application(Frame):

    def __init__(self, master):
        """ Initialize frame"""
        super(Application, self).__init__(master)
        self.create_widgets()

    def create_widgets(self):
        """Create 3 useless buttons"""

        a = Button(text="Browse Excel File", bd='5', command=self.browse)
        a.place(relx=0.5, rely=0.1, anchor=CENTER)

        #   BROWSE EXCEL DOCUMENT

    def browse(self):

        files = filedialog.askopenfilenames(initialdir="/Desktop", title="Browse Files", filetypes=(("all files", "*.*"),))


        for f in files:
            if fnmatch.fnmatch(f, '*(1).jpg'):
                print(f)
                os.remove(f)
            if fnmatch.fnmatch(f, '*(2).jpg'):
                print(f)
                os.remove(f)
            if fnmatch.fnmatch(f, '*(3).jpg'):
                print(f)
                os.remove(f)
            if fnmatch.fnmatch(f, '*Copy.jpg'):
                print(f)
                os.remove(f)

    def client_exit(self):
        root.destroy()

    def help(self):
        tk.messagebox.showinfo("How to Guide", "1.) Meme")

root = Tk()

root.title("OCR to Leapfrog GUI")
root.geometry("300x300")
app = Application(root)
root.mainloop()


