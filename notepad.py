import os.path
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

notepadd = Tk()
notepadd.geometry("700x500")
notepadd.title("Untitled - Notepad")


def newfile(event=None):
    global file

    if (len(Textarea.get(1.0, END))) != 1:
        result = tmsg.askyesnocancel("Save Dialog Box!", "Do you want to save the file")
        if result is True:
            savefile(event)
            Textarea.delete(1.0, END)
            notepadd.title("Untitled - Notepad")
        elif result is False:
            file = None
            Textarea.delete(1.0, END)
            notepadd.title("Untitled - Notepad")
        elif result is None:
            pass
    else:
        file = None
        Textarea.delete(1.0, END)
        notepadd.title("Untitled - Notepad")


def openfile(event=None):

    global file
    if file is not None:
        result = tmsg.askyesnocancel("Save Dialog Box!", "Do you want to save the file")
        if result is True:
            savefile(event)
        elif result is False:
            file = askopenfilename(defaultextension=".txt",
                                   filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            if file == "":
                pass
            else:
                if ".txt" not in file:
                    Textarea.insert(INSERT,
                                    "ERROR OCCURED WHILE OPENING FILE\nERROR TYPE = EXTENSION OTHER THAN '.txt'")
                else:
                    notepadd.title(os.path.basename(file) + " - Notepad")
                    Textarea.delete(1.0, END)
                    y = open(file, "r")
                    Textarea.insert(1.0, y.read())
                    y.close()
        elif result is None:
            pass
    elif file is None:
        file = askopenfilename(defaultextension=".txt",
                               filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            pass
        else:
            if ".txt" not in file:
                Textarea.insert(INSERT,
                                "ERROR OCCURED WHILE OPENING FILE\nERROR TYPE = EXTENSION OTHER THAN '.txt'")
            else:
                notepadd.title(os.path.basename(file) + " - Notepad")
                Textarea.delete(1.0, END)
                f = open(file, "r")
                Textarea.insert(1.0, f.read())
                f.close()


def savefile(event=None):
    global file
    if file is None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                                                                 ("Text Documents",
                                                                                                  "*.txt")])
        if file == "":
            pass
        else:
            f = open(file, "w")
            f.write(Textarea.get(1.0, END))
            f.close()
            tmsg.showinfo("Notepad", "File has been saved")
            notepadd.title(os.path.basename(file) + " - Notepad")
    else:
        f = open(file, "w")
        f.write(Textarea.get(1.0, END))
        tmsg.showinfo("Notepad", "File has been saved")
        f.close()


def quitapp(event=None):
    notepadd.destroy()


def cut():
    Textarea.event_generate("<<Cut>>")


def copy():
    Textarea.event_generate("<<Copy>>")


def paste():
    Textarea.event_generate("<<Paste>>")


def allselect():
    Textarea.tag_add("start", "1.0", "end")
    Textarea.tag_configure("start", background="DodgerBlue2", foreground="white")


def about():
    tmsg.showinfo("Notepad", "Created by :- Manish Aggarwal \nDate of creation :- 04-Aug-21")


def helpp(event=None):
    tmsg.showinfo("Notepad", "Contact = 91+ 8368577397")


scroll = Scrollbar(notepadd)
scroll.pack(side="right", fill=Y)
Textarea = Text(notepadd, font="Consolas 13", yscrollcommand=scroll.set)
Textarea.pack(fill="both")

MenuBar = Menu(notepadd)
file = None
filemenu = Menu(MenuBar, tearoff=0)
filemenu.add_command(label="New", command=newfile, accelerator="Ctrl+N")
notepadd.bind("<Control-n>", newfile)
filemenu.add_command(label="Open", command=openfile, accelerator="Ctrl+O")
notepadd.bind("<Control-o>", openfile)

filemenu.add_command(label="Save", command=savefile, accelerator="Ctrl+S")
notepadd.bind("<Control-s>", savefile)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=quitapp, accelerator="Ctrl+Q")
notepadd.bind("<Control-q>", quitapp)

MenuBar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(MenuBar, tearoff=0)
editmenu.add_command(label="Cut", command=cut, accelerator="Ctrl+X")
editmenu.add_command(label="Copy", command=copy, accelerator="Ctrl+C")
editmenu.add_command(label="Paste", command=paste, accelerator="Ctrl+V")
editmenu.add_command(label="Select all", command=allselect)
MenuBar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(MenuBar, tearoff=0)
helpmenu.add_command(label="About Notepad", command=about)
helpmenu.add_command(label="Help", command=helpp, accelerator="Ctrl+H")
notepadd.bind("<Control-h>", helpp)

MenuBar.add_cascade(label="Help", menu=helpmenu)

notepadd.config(menu=MenuBar)
scroll.config(command=Textarea.yview)

notepadd.mainloop()
