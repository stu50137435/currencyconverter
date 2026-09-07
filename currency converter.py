#from old attempt
from tkinter import *

window = Tk()
window.geometry("200x300")

LBL_pounds = Lable(window, Text="pounds")
LBL_pounds.pack()

txt_pounds = Entry(window, width=15)
txt_pounds.pack

bnt_convert = Button(window, text="convert")
bnt_convert.pack(pady = 10)

LBL_euros = Entry(window, Text = "euros")
LBL_euros.pack()

txt_euros = Entry(window, width=15)
txt_euros.pack()


window.mainloop()