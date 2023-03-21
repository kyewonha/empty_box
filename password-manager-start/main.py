from tkinter import *
#위에는 클래스 아래는 모듈
from tkinter import messagebox
import random
import pyperclip


# pyper

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    input3.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letters_list= [random.choice(letters) for _ in range(nr_letters)]
    symbols_list= [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list= [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list)
    # print(password_list)

    x="".join(password_list)
    pyperclip.copy(x)
    input3.insert(0, x)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_input = input1.get()
    email_input = input2.get()
    password_input = input3.get()

    if len(website_input)==0 or len(password_input)==0:
        messagebox.showinfo(title='Oops', message="you have left fields empty")
    else:
        is_ok= messagebox.askokcancel(title='want to save?', message=f"These are the details entered: \nEmail: {email_input}"
                               f"\nPassword: {password_input} \n Is it ok to save?")
        '''
        
        with 문을 쓰는 이유. f로 묶어서 연속 작업을 하기 편하고
        with문이 종료됨과 동시에 f.close()가 자동 작동
        tkinter의 entry 값을 불러오기 위해 input1.get()문 사용
        '''
        if is_ok:
            with open('data.txt', 'a') as f:
                f.write(f'{website_input} | {email_input} | {password_input} \n')
                #버튼이 눌리고 내용을 비워주기 작동이 완료됨을 확인하는 효과도 있네
                input1.delete(0 ,END)
                # input2.delete(0,END)
                input3.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title("password manager")
window.config(padx=40, pady= 40)
canvas = Canvas(width=200, height=200)
lock = PhotoImage(file= 'logo.png')
canvas.create_image(100,100, image=lock)
canvas.grid(column=1, row=0)

website= Label(text="Website:")
website.grid(column=0, row=1)

input1= Entry(width=35)
input1.grid(column=1, row=1, columnspan=2)
input1.focus() # 마우스 시작커서 잡아주기

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

# email.insert(END, "you22th@naver.com")

input2 = Entry(width=35)
input2.grid(column=1, row=2, columnspan=2)
input2.insert(0, "you22th@naver.com")

password= Label(text="Password:")
password.grid(row=3, column=0)

input3= Entry()
input3.grid(row=3, column=1)

password_button = Button(text="Generate password" , command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()