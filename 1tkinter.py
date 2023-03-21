# import tkinter
import tkinter
from tkinter import *
def button_clicked():
    print('i got clicked')
    #config는 업데이트를 해준다.
    new_text= input.get()
    my_label.config(text=new_text)
window = Tk()
window.title("MY FIRST GUI PROGRAM")
window.minsize(width=500, height=300)

my_label= Label(text="I am a label", font=("Arial",24,'bold'))
my_label.grid(column=0, row=0)

my_label['text']= "new text"
my_label.config(text='new text')

button = Button(text='Click me',command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text='new button')
button2.grid(column=2, row=0)
input = Entry(width=10)
input.grid(column=3,row=2)
print(input.get())









window.mainloop()