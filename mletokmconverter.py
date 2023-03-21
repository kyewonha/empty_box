from tkinter import *

def changekm():
    miles= float(entry.get())
    km = miles * 1.689
    label_4.config(text=f'{km}')

window= Tk()
window.title("mile_to_km_converter")
window.config(padx=20, pady=20)


entry= Entry(width =7)
entry.grid(column=1, row=0)

label_1 = Label(text='miles')
label_1.grid(column=2, row=0)

label_2 = Label(text='is equal to')
label_2.grid(column=0, row=1)

label_3 = Label(text='km')
label_3.grid(column=2, row=1)

label_4 = Label(text='0')
label_4.grid(column=1, row=1)

button = Button(text='Click me',command=changekm)
button.grid(column=1, row=2)

window.mainloop()