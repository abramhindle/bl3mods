from __Generate_Hotfix import ModHeader, JSONInfo, Search, HotFix
from bl3data import BL3Data
import os
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
data = BL3Data()

#This is used as a referencesto look and see what are the names of the game folders
FileNames = ["Alisma", "CohtmlPlugin", "Config", "Content", "Dandelion", "DatasmithContent", "Engine", "Game", "GbxAI", "GbxBlockingVolumes", "GbxGameSystemCore", "GbxJira",
             "GbxSharedBlockoutAssets", "GbxSpawn", "Geranium", "Hibiscus", "HoudiniEngine", "Ixora", "MediaCompositing", "OakGame", "Paper2D", "WwiseEditor"]  # stores folder names

#the user is able to choose a json file
def FileChoice():
    file = askopenfilename(filetypes=[("Choose file", ".json")])
    # Removes the files extention, as we dont need it
    raw_path = os.path.splitext(file)[0]
    i = 0
    index = 0
    while index <= 0:
        Find = "/" + FileNames[i]
        i += 1
        if Find in raw_path:
            index = raw_path.find(Find)
    # this is the data we need to pass in information
    True_Path = raw_path[index::]
    JSONInfo(True_Path)

#Creates a new window for the user to see and for the commands to be used


def NeWindow(func):
    #these variables will determine how many things to add to the window as i need them
    l = 0
    e = 0
    b = 0
    lb = 0
    Nwindow = Tk()

    #used to grab the values the then entry textvariables, so that for any function I can call them and reuse them
    def get_val():
        a, b, c, d, e, f = entry1.get(), entry2.get(), 
        entry3.get(), entry4.get(), entry5.get(), entry6.get()
        ModHeader(a, b, c, d, e, f)
    #generics we can reuse for any task I have created
    entry1 = StringVar(Nwindow)
    entry2 = StringVar(Nwindow)
    entry3 = StringVar(Nwindow)
    entry4 = StringVar(Nwindow)
    entry5 = StringVar(Nwindow)
    entry6 = StringVar(Nwindow)

    #attempting to use generics to make my life easier
    #this will change a lot later on, but for now i will try to get it to work
    if func == ModHeader:  # creates a mod file of you to use
        Nwindow.title("Mod Header")
        text1 = 'Name of the hotfix file: '
        text2 = 'The actual mod name: '
        text3 = 'Author(s) name: '
        text4 = 'Discription: '
        text5 = 'Version of this mod: '
        text6 = 'The catagory in which this mods fits to: '
        b1text = 'Create Mod Header'
        def b1command(): return get_val()
        l = 6
        e = 6
        b = 1
    elif func == JSONInfo:  # this will be more fleshed out later, but for now it I am trying to get the interfce to work
        Nwindow.title("Look Through File information")
        b1text = "Choose file"
        def b1command(): return FileChoice()
        l = 0
        e = 0
        b = 1
    elif func == Search:
        None
    elif func == HotFix:
        None

    #this is the best way for the program to reuse generics, while being able to determine how many are needed for a paticular program
    if l >= 1:
        Label(Nwindow, text=text1).grid(row=0)
        if l >= 2:
            Label(Nwindow, text=text2).grid(row=1)
            if l >= 3:
                Label(Nwindow, text=text3).grid(row=2)
                if l >= 4:
                    Label(Nwindow, text=text4).grid(row=3)
                    if l >= 5:
                        Label(Nwindow, text=text5).grid(row=4)
                        if l >= 6:
                            Label(Nwindow, text=text6).grid(row=5)
    if e >= 1:
        Entry(Nwindow, textvariable=entry1).grid(row=0, column=1)
        if e >= 2:
            Entry(Nwindow, textvariable=entry2).grid(row=1, column=1)
            if e >= 3:
                Entry(Nwindow, textvariable=entry3).grid(row=2, column=1)
                if e >= 4:
                    Entry(Nwindow, textvariable=entry4).grid(row=3, column=1)
                    if e >= 5:
                        Entry(Nwindow, textvariable=entry5).grid(
                            row=4, column=1)
                        if e >= 6:
                            Entry(Nwindow, textvariable=entry6).grid(
                                row=5, column=1)
    if b >= 1:
        Button(Nwindow, font=("Times New Roman", 18),
               text=b1text, command=b1command).grid(row=6)
    if lb == 1:
        Listbox(Nwindow)


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Hot Fix Generator")
    # window.geometry("500x500")
    Button(text="1. Mod Header", font=("Times New Roman", 18),
           command=lambda: NeWindow(ModHeader))
    Button(text="2. Choose File", font=("Times New Roman", 18),
           command=lambda: NeWindow(JSONInfo))
    Button(text="3. Find All References", font=(
        "Times New Roman", 18), command=lambda: NeWindow(Search))
    Button(text="4. Make Regular Hotfix", font=(
        "Times New Roman", 18), command=lambda: NeWindow(HotFix))

    #this will pack everything so that I do not have to do it every time
    for c in sorted(window.children):
        window.children[c].pack()
    window.mainloop()