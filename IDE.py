from tkinter import *
from tkinter.scrolledtext import ScrolledText
from subprocess import Popen, PIPE


def donothing():

    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()

def run_command( str_obj ,output_text ):

    # Create a Python file for input to python interpreter

    output_text.delete('1.0', END)

    file_index = open("file.py", "w")

    file_index.write(str_obj)

    # Close opend file
    file_index.close()

    p = Popen(['C:\Python\python.exe', 'file.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE)

    output, err = p.communicate()
    output = str(output)
    err = str(err)
    output = output.strip("b'")
    output = output.replace('\\n', '')
    output = output.replace('\\r', '')
    err = err.strip("b'")
    err = err.replace('\\n', '')
    err = err.replace('\\r', '')

    output_text.insert(INSERT, output + err )

    rc = p.returncode
    return output

def clear_input (input_text):

    input_text.delete('1.0', END)

def clear_output (output_text):

    output_text.delete('1.0', END)



if __name__== "__main__":

    root = Tk()
    root.title("Light Python Interpreter")
    root.geometry("1350x650")
    #root.resizable(0, 0)

    Label(root, text="Python Interpreter", height=3, fg="red", font="Times 15 bold", bg="yellow", ).grid(row=0,
                                                                                                         column=20)

    Label(root, text="Write your program Here :", font="Verdana 12 bold").grid(row=1, column=0)
    Label(root, text="Output:", font="Verdana 12 bold").grid(row=1, column=30)

    #input_text = ScrolledText(root, width=70)
    input_text = ScrolledText(wrap=WORD, width=70)

    input_text.grid(row=2, column=0)

    # nter_value = input_text.get("1.0",END)

    output_text = ScrolledText(wrap=WORD, width=70)

    output_text.grid(row=2, column=30)

    B1 = Button(root, text="Run", fg="red", bg="lime", font="Verdana 15 bold",
               command=lambda: run_command(input_text.get("1.0", END),output_text))

    B2 = Button(root, text="Clear Output ", fg="red", bg="lime", font="Verdana 15 bold",
                command=lambda: clear_output(output_text))

    B3 = Button(root, text="Clear Input ", fg="red", bg="lime", font="Verdana 15 bold",
                command=lambda: clear_input(input_text))


    B1.grid(row=100, column=20)

    B2.grid(row=100, column=30)

    B3.grid(row=100, column=0)


    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_command(label="Save as...", command=donothing)
    filemenu.add_command(label="Close", command=donothing)

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)

    editmenu.add_separator()

    editmenu.add_command(label="Cut", command=donothing)
    editmenu.add_command(label="Copy", command=donothing)
    editmenu.add_command(label="Paste", command=donothing)
    editmenu.add_command(label="Delete", command=donothing)
    editmenu.add_command(label="Select All", command=donothing)

    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)
    root.mainloop()


