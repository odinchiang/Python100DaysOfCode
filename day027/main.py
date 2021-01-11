# https://docs.python.org/3/library/tkinter.html#the-packer
# http://tcl.tk/man/tcl8.6/TkCmd/pack.htm
# http://tcl.tk/man/tcl8.6/TkCmd/entry.htm
# http://tcl.tk/man/tcl8.6/TkCmd/label.htm

from tkinter import *

window = Tk()
window.title("My First GUI Program")
# 視窗最小寬高
window.minsize(width=500, height=300)
# 視窗的 padding
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "normal"))
# my_label.pack(side="left")
# my_label.pack()
# my_label.place(x=0, y=0)  # 視窗左上角為(0, 0)
my_label.grid(row=0, column=0)
my_label.config(padx=2, pady=2)

my_label["text"] = "New Text"
my_label.config(text="New New Text")


# Button

def button_clicked():
    print("I got clicked")
    my_label["text"] = "Button Got Clicked"
    my_label["text"] = input.get()


button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(row=1, column=1)

new_button = Button(text="New Button")
new_button.grid(row=0, column=2)

# Entry
input = Entry(width=10)
# input.pack()
input.grid(row=2, column=3)





# 保持視窗開啟
window.mainloop()
