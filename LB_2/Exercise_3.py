from tkinter import messagebox
import tkinter as rypli

own = 0
money_salary = 0
vion_1=0
vion_2=0
vion_3=0 



def f_1rt(): ## функция переноса данных из списка 1
    global grade_1
    grade_1 = int(grade_var_1.get())

def f_2rt(): ## функция переноса данных из списка 2
    global grade_2
    grade_2 = int(grade_var_2.get())

##3.1
def G_1tyr(): ## функция переноса данных языка
    global BCA_1, vion_1
    vion_1 = int(BCA_1.get())

##3.2
def G_2tyr(): ## функция переноса данных языка
    global BCA_2, vion_2
    vion_2 = int(BCA_2.get())

##3.3
def G_3tyr(): ## функция переноса данных языка
    global BCA_3, vion_3
    vion_3 = int(BCA_3.get())

def result():
    global age, grade_1, grade_2, vion_1, vion_2, vion_3, money_salary, own, nexp_1, nexp_2, nexp_3
    own = vion_1 + vion_2 + vion_3
    money_salary = 15000
    try:
        age = int(lktn_8.get())
        if (age >= 18): 
            if (grade_1 == 1): 
                messagebox.showinfo('Результат', 'Уважаемый(ая), вы нам не подходите. Попытайте удачу в другом месте или подстройтесь под необходимые требования в дальнейшем. Удачи.')
            elif (grade_1 == 2):
                messagebox.showinfo('Результат', 'Уважаемый(ая), вы нам не подходите. Попытайте удачу в другом месте или подстройтесь под необходимые требования в дальнейшем. Удачи.')
            elif (grade_1 == 3):
                money_salary = int(money_salary) + 1200
                if (grade_2 == 1):
                    messagebox.showinfo('Результат', 'Уважаемый(ая), вы нам не подходите. Попытайте удачу в другом месте или подстройтесь под необходимые требования в дальнейшем. Удачи.')
                elif (grade_2 == 2):
                    money_salary = int(money_salary) + 3000
                    if (own == 0):
                        messagebox.showinfo('Результат', 'Уважаемый(ая), вы нам не подходите. Попытайте удачу в другом месте или подстройтесь под необходимые требования в дальнейшем. Удачи.')
                    elif (own == 1):
                        money_salary = int(money_salary) + 1500
                        print(money_salary)
                        messagebox.showinfo('Результат', 'Поздравляем, Вы нам подходите и мы с удовольствием ждем Вас на уже запланированное собеседование. Отправьте свои результаты по электронной почте нашей компании. Удачи :)')
                    elif (own == 2):
                        money_salary = int(money_salary) + 2000
                        print(money_salary)
                        messagebox.showinfo('Результат', 'Поздравляем, Вы нам подходите и мы с удовольствием ждем Вас на уже запланированное собеседование. Отправьте свои результаты по электронной почте нашей компании. Удачи :)')
                    elif (own == 3):
                        money_salary = int(money_salary) + 7000
                        print(money_salary)
                        messagebox.showinfo('Результат', 'Поздравляем, Вы нам подходите и мы с удовольствием ждем Вас на уже запланированное собеседование. Отправьте свои результаты по электронной почте нашей компании. Удачи :)')
                    else:
                        print('ошибка')
                elif (grade_2 == 3):
                    money_salary = int(money_salary) + 7000
                    if (own == 0):
                        messagebox.showinfo('Результат', 'Уважаемый(ая), вы нам не подходите. Попытайте удачу в другом месте или подстройтесь под необходимые требования в дальнейшем. Удачи.')
                    elif (own == 1):
                        money_salary = int(money_salary) + 1500
                        print(money_salary)
                        messagebox.showinfo('Результат', 'Поздравляем, Вы нам подходите и мы с удовольствием ждем Вас на уже запланированное собеседование. Отправьте свои результаты по электронной почте нашей компании. Удачи :)')
                    elif (own == 2):
                        money_salary = int(money_salary) + 2000
                        print(money_salary)
                        messagebox.showinfo('Результат', 'Поздравляем, Вы нам подходите и мы с удовольствием ждем Вас на уже запланированное собеседование. Отправьте свои результаты по электронной почте нашей компании. Удачи :)')
                    elif (own == 3):
                        money_salary = int(money_salary) + 7000
                        print(money_salary)
                        messagebox.showinfo('Результат', 'Поздравляем, Вы нам подходите и мы с удовольствием ждем Вас на уже запланированное собеседование. Отправьте свои результаты по электронной почте нашей компании. Удачи :)')
                    else:
                        print('ошибка')
                else:
                    print('ошибка')
            elif (grade_1 == 4): 
                money_salary = int(money_salary) + 5000
                if (grade_2 == 1):
                    messagebox.showinfo('Результат', 'Уважаемый(ая), вы нам не подходите. Попытайте удачу в другом месте или подстройтесь под необходимые требования в дальнейшем. Удачи.')
                elif (grade_2 == 2):
                    money_salary = int(money_salary) + 3000
                    if (own == 0):
                        messagebox.showinfo('Результат', 'Уважаемый(ая), вы нам не подходите. Попытайте удачу в другом месте или подстройтесь под необходимые требования в дальнейшем. Удачи.')
                    elif (own == 1):
                        money_salary = int(money_salary) + 1500
                        print(money_salary)
                        messagebox.showinfo('Результат', 'Поздравляем, Вы нам подходите и мы с удовольствием ждем Вас на уже запланированное собеседование. Отправьте свои результаты по электронной почте нашей компании. Удачи :)')
                    elif (own == 2):
                        money_salary = int(money_salary) + 2000
                        print(money_salary)
                        messagebox.showinfo('Результат', 'Поздравляем, Вы нам подходите и мы с удовольствием ждем Вас на уже запланированное собеседование. Отправьте свои результаты по электронной почте нашей компании. Удачи :)')
                    elif (own == 3):
                        money_salary = int(money_salary) + 7000
                        print(money_salary)
                        messagebox.showinfo('Результат', 'Поздравляем, Вы нам подходите и мы с удовольствием ждем Вас на уже запланированное собеседование. Отправьте свои результаты по электронной почте нашей компании. Удачи :)')
                    else:
                        print('ошибка')
                elif (grade_2 == 3):
                    money_salary = int(money_salary) + 7000
                    if (own == 0):
                        messagebox.showinfo('Результат', 'Уважаемый(ая), вы нам не подходите. Попытайте удачу в другом месте или подстройтесь под необходимые требования в дальнейшем. Удачи.')
                    elif (own == 1):
                        money_salary = int(money_salary) + 1500
                        print(money_salary)
                        messagebox.showinfo('Результат', 'Поздравляем, Вы нам подходите и мы с удовольствием ждем Вас на уже запланированное собеседование. Отправьте свои результаты по электронной почте нашей компании. Удачи :)')
                    elif (own == 2):
                        money_salary = int(money_salary) + 2000
                        print(money_salary)
                        messagebox.showinfo('Результат', 'Поздравляем, Вы нам подходите и мы с удовольствием ждем Вас на уже запланированное собеседование. Отправьте свои результаты по электронной почте нашей компании. Удачи :)')
                    elif (own == 3):
                        money_salary = int(money_salary) + 7000
                        print(money_salary)
                        messagebox.showinfo('Результат', 'Поздравляем, Вы нам подходите и мы с удовольствием ждем Вас на уже запланированное собеседование. Отправьте свои результаты по электронной почте нашей компании. Удачи :)')
                    else:
                        print('ошибка')
                else:
                    print('ошибка')
            else:
                print('ошибка')     
        else:
            messagebox.showinfo('Результат', 'Уважаемый(ая), вы нам не подходите. Попытайте удачу в другом месте или подстройтесь под необходимые требования в дальнейшем. Удачи.')
    except:
        messagebox.showinfo('Внимание', 'Упс... возможно ошибка данных, проверьте поля')
    
    
    


win = rypli.Tk()
win.geometry("255x641+300+100")
win.overrideredirect(False)

############################################################################################################################################

lktn_1 = rypli.Label(win, text = "Фамилия: ")
lktn_1.grid(row=0,column=0, sticky = "e", padx=5, pady=5)
lktn_2 = rypli.Label(win, text = "Имя: ")
lktn_2.grid(row=1,column=0, sticky = "e", padx=5, pady=5)
lktn_3 = rypli.Label(win, text = "Отчество: ")
lktn_3.grid(row=2,column=0, sticky = "e", padx=5, pady=5)
lktn_4 = rypli.Label(win, text = "Возраст: ")
lktn_4.grid(row=3, column=0, sticky = "e", padx=5, pady=5)

lktn_5 = rypli.Entry(win)
lktn_5.grid(row=0, column=1, padx=5, pady=5)
lktn_6 = rypli.Entry(win)
lktn_6.grid(row=1, column=1, padx=5, pady=5)
lktn_7 = rypli.Entry(win)
lktn_7.grid(row=2, column=1, padx=5, pady=5)
lktn_8 = rypli.Entry(win)
lktn_8.grid(row=3, column=1, padx=5, pady=5)

############################################################################################################################################
    
lktn_7 = rypli.Label(win, bg = "#000000", height=1, bd=0)
lktn_7.grid(row=4, column=0, columnspan = 2,  sticky="we", padx=5, pady=5)

############################################################################################################################################

lktnB_8 = rypli.Label(win, text = "Укажите ваше образование : ")
lktnB_8.grid(row=5, column=0, columnspan=2, sticky="we", padx=5, pady=5)

grade_var_1 = rypli.IntVar()
rypli.Radiobutton(win, text = "Начальное", variable = grade_var_1, value = 1, command = f_1rt).grid(row=6, column=0, sticky = "w")
rypli.Radiobutton(win, text = "Среднее", variable = grade_var_1, value = 2, command = f_1rt).grid(row=7, column=0, sticky = "w")
rypli.Radiobutton(win, text = "Среднее высшее", variable = grade_var_1, value = 3, command = f_1rt).grid(row=8, column=0, sticky = "w")
rypli.Radiobutton(win, text = "Высшее", variable = grade_var_1, value = 4, command = f_1rt).grid(row=9, column=0, sticky = "w")

############################################################################################################################################

lktn_9 = rypli.Label(win, bg = "#000000", height=1, bd=0)
lktn_9.grid(row=10, column=0, columnspan = 2,  sticky="we", padx=5, pady=5)

############################################################################################################################################

lktn_10 = rypli.Label(win, text = "Ваш опыт работы : ")
lktn_10.grid(row=11, column=0, columnspan=2, sticky="we", padx=5, pady=5)

grade_var_2 = rypli.IntVar()
rypli.Radiobutton(win, text = "менее 3-х лет", variable = grade_var_2, value = 1, command = f_2rt).grid(row=12, column=0, sticky = "w")
rypli.Radiobutton(win, text = "от 3 до 5 лет", variable = grade_var_2, value = 2, command = f_2rt).grid(row=13, column=0, sticky = "w")
rypli.Radiobutton(win, text = "Более 5-и лет", variable = grade_var_2, value = 3, command = f_2rt).grid(row=14, column=0, sticky = "w")

############################################################################################################################################

lktn_11 = rypli.Label(win, bg = "#000000", height=1, bd=0)
lktn_11.grid(row=15, column=0, columnspan = 2,  sticky="we", padx=5, pady=5)

############################################################################################################################################

lktn_12 = rypli.Label(win, text = "Какие языки вы знаете :")
lktn_12.grid(row=16, column=0, columnspan=2, sticky="we", padx=5, pady=5)

BCA_1 = rypli.IntVar()
C_1 = rypli.Checkbutton(win, text = "Английский", variable=BCA_1, command = G_1tyr)
C_1.grid(row=17, column=0, padx=5, pady=5, sticky = "w")

BCA_2 = rypli.IntVar()
C_2 = rypli.Checkbutton(win, text = "Испанский", variable=BCA_2, command = G_2tyr)
C_2.grid(row=18, column=0, padx=5, pady=5, sticky = "w")

BCA_3 = rypli.IntVar()
C_3 = rypli.Checkbutton(win, text = "Французкий", variable=BCA_3, command = G_3tyr)
C_3.grid(row=19, column=0, padx=5, pady=5, sticky = "w")

############################################################################################################################################

lktn_13 = rypli.Label(win, bg = "#000000", height=1, bd=0)
lktn_13.grid(row=20, column=0, columnspan = 2,  sticky="we", padx=5, pady=5)

############################################################################################################################################

lktn_14 = rypli.Button(win, text = "Отмена")
lktn_14.grid(row=21, column=0, padx=5, pady=5, sticky = "wens")

lktn_15 = rypli.Button(win, text = "Завершить", command=result)
lktn_15.grid(row=21, column=1, padx=5, pady=5, sticky = "wens")


win.mainloop()










