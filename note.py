from tkinter import*
from tkinter import filedialog,messagebox,simpledialog
top=Tk()
top.title("Notepad by JK")
top.geometry("600x500")
import os

name=simpledialog.askstring("Enter data","what is your name?",parent=top)
if name is not None:
    top.title("notrpad by "+ name)

editor=Text(top,width=600)
editor.pack()

def newFile():
    editor.delete(1.0,END)

def closeJKNotepad():
    fd=messagebox.askyesno("Confirm?",message="are you really want to close me?" )
    if fd:
       top.quit() 

filetypes=(("text File","*.txt"), ("All Files","*.*") ) 

def Openfile():
    global filetypes 
    fd=filedialog.askopenfile(title="Open file here",filetypes=filetypes)
    editor.insert(1.0,fd.readlines())   # type: ignore


def saveFille():
    global filetypes
    fd=filedialog.asksaveasfile(title="Save file here",filetypes=filetypes)
    editor.insert(1.0,fd.readlines())  #type: ignore
    if fd is None:
        return
    fd.write(editor.get(0.0,END))
    fd.close()    


menubar=Menu(top)    

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=newFile)
filemenu.add_command(label="New Window")
filemenu.add_command(label="Open" ,command=Openfile)
filemenu.add_command(label="Save",command=saveFille)
filemenu.add_command(label="Save As")
filemenu.add_separator()
filemenu.add_command(label="Page Setup")
filemenu.add_command(label="Print")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=closeJKNotepad)

editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="Undo",state=DISABLED)
editmenu.add_command(label="Cut          Ctrl+X",state=DISABLED)
editmenu.add_command(label="Copy         Ctrl+C",state=DISABLED)
editmenu.add_command(label="Paste        Ctrl+V",state=DISABLED)
editmenu.add_command(label="Delete",state=DISABLED)
editmenu.add_separator()
editmenu.add_command(label="Find",state=DISABLED)
editmenu.add_command(label="Find next",state=DISABLED)
editmenu.add_command(label="Find Prevoius",state=DISABLED)
editmenu.add_command(label="Replace",state=DISABLED)
editmenu.add_command(label="Go to")
editmenu.add_separator()
editmenu.add_command(label="Select all")
editmenu.add_command(label="Date/Time")
editmenu.add_command(label="Font")

viewmenu=Menu(menubar,tearoff=0)
zoommenu=Menu(viewmenu,tearoff=0)
zoommenu.add_command(label="zoom in")
zoommenu.add_command(label="zoom out")

viewmenu.add_cascade(label="Zoom",menu=zoommenu)
viewmenu.add_command(label="Status bar")
viewmenu.add_checkbutton(label="Word Wrap")



footerText=StringVar()
footerText.set("Ln 1, Col 1\t|\t100%\tWindow(CRLF)\t\t|\tUTF-8")
footer=Label(top,textvariable=footerText,bd=1,relief=SUNKEN,anchor="w",padx=10,fg="gray",font=("Arial",10))
footer.pack(side=BOTTOM,fill=X)

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit",menu=editmenu)
menubar.add_cascade(label="View",menu=viewmenu)

top.config(menu=menubar)
top.mainloop()