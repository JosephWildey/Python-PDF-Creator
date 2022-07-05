from PIL import Image,ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from fpdf import FPDF

frame = tk.Tk()
frame.title("Word Editor")

inputtxt = tk.Text(frame, height = 75, width = 175)

global user_image
user_image = ""

def donothing():
    x = 0

def generate_PDF():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, inputtxt.get(1.0, "end-1c"))
    pdf.image(user_image)
    pdf.output('tuto1.pdf', 'F')

def select_file():

    global user_image

    filetypes = (
         ('text files', '*.txt'), 
         ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file', 
        initialdir='/', 
        filetypes=filetypes
    )

    showinfo(
        title='Selected File', 
        message=filename
    )
    
    img_to_insert = ImageTk.PhotoImage(file=filename)

    inputtxt.image_create("current", image=img_to_insert)

    user_image = filename

# create a menubar
menubar = tk.Menu(frame)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Import", command=select_file)
filemenu.add_command(label="Save", command=generate_PDF)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=frame.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

inputtxt.pack()

frame.config(menu=menubar)

frame.mainloop()
