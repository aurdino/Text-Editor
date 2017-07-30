import Tkinter
from Tkinter import *
import pygame 
from pygame.locals import *
import tkFileDialog as filedialog
import ttk
#pygame.init()
#pygame.font.init()
import tkMessageBox



root = Tk()
root.minsize(640,600)
root.geometry("100x100")
root.title("Text Editor")

text = Text(root,width = 400,height = 350,font = ("Andale Mono",12),bd = 2)
text.pack()



def new():
	ans = tkMessageBox.askquestion("title = Save File",message = "Would you like to save this file")
	if ans is True:
		save()
	else:
		delete_all()

def open_file():
	new()
	file = filedialog.askopenfile()
	text.insert(INSERT,file.read())

def save():
	path = filedialog.asksaveasfilename()
	write = open(path,mode='w')
	write.write(text.get("1.0"),END)

def rename():
	pass


def close():
	save()
	root.quit()


def cut():
	root.clipboard_clear()
	text.clipboard_append(string = text.selection_get())
	text.delete(index1 = SEL_FIRST,index2 = SEL_LAST)

def copy():
	root.clipboard_clear()
	text.clipboard_append(string = text.selection_get())

def paste():
	text.insert(INSERT,root.clipboard_get())


def delete():
	text.delete(index1 = SEL_FIRST,index2 = SEL_LAST)

def select_all():
	text.tag_add(SEL,"1.0",END)



def undo():
	pass

def redo():
	pass


def delete_all():
	text.delete(1.0,END)

#file menu

menu = Menu(root)
root.config(menu = menu)
file_menu = Menu(menu)
menu.add_cascade(label = "File",menu = file_menu)

file_menu.add_command(label = "New",command = new)
file_menu.add_command(label = "Open",command = open_file)

file_menu.add_separator()
file_menu.add_command(label = "Close",command = close)
file_menu.add_command(label = "Save | clt+s",command = save)
file_menu.add_command(label = "Rename",command = rename)

# Edit menu

edit_menu = Menu(menu)
menu.add_cascade(label = "Edit",menu = edit_menu)
edit_menu.add_command(label = 'Undo',command = undo)
edit_menu.add_command(label = 'Redo',command = redo)
edit_menu.add_separator()
edit_menu.add_command(label = 'Copy',command = copy)
edit_menu.add_command(label = 'Cut',command = cut)
edit_menu.add_command(label = 'Paste',command = paste)
edit_menu.add_command(label = 'Delete',command = delete)
edit_menu.add_separator()
edit_menu.add_command(label = 'Select All',command = select_all)
edit_menu.add_command(label = 'Delate All',command = delete_all)



root.mainloop()
