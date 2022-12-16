import tkinter as rtyp
kto = 0
def topl():
    btly_3.config(state="readonly")
    btly_4.config(state="readonly")
def f_1rt(): ## функция переноса данных из списка 1 
    global grade_1
    grade_1 = grade_var_1.get()
    print(f'Ответ задачи №1: {grade_1}')
def f_2rt(): ## функция переноса данных из списка 2 
    global grade_2
    grade_2 = grade_var_2.get()
    print(f'Ответ задачи №2: {grade_2}')
def f_3rt(): ## функция переноса данных из списка 3 
    global grade_3
    grade_3 = grade_var_3.get()
    print(f'Ответ задачи №3: {grade_3}')
def f_4rt(): ## функция переноса данных из списка 4 
    global grade_4
    grade_4 = grade_var_4.get()
    print(f'Ответ задачи №4: {grade_4}')
def f_5rt(): ## функция переноса данных из списка 5 
    global grade_5
    grade_5 = grade_var_5.get()
    print(f'Ответ задачи №5: {grade_5}')
def f_6rt(): ## функция переноса данных из списка 6 
    global grade_6
    grade_6 = grade_var_6.get()
    print(f'Ответ задачи №6: {grade_6}')
## по условию задания, нужно определить только группу по оценкам,
## переменные zbty_1 и zbty_2 не редактировал, только вывел
def conclusion():
    try:
        global zbty_1, zbty_2, kto
        zbty_1 = btly_3.get()
        zbty_2 = btly_4.get()
        kto = grade_1 + grade_2 + grade_3 + grade_4 + grade_5 + grade_6
        if ((zbty_1 == '') and (zbty_2 == '')):
            btly_14['text'] = "Ошибка, недостаточно \n данных"
        else:
            if ((grade_1 == 3) and (grade_2 == 3) and (grade_3 == 3) and (grade_4 == 3) and (grade_5 == 3) and (grade_6 == 3)):
                topl()
                btly_14['text'] = f"Имя: {zbty_1}\n Учебные данные: {zbty_2}\nКатегория: 1"
                btly_14['width'] = "21"
## необходимо доработать условие для более точного логического входа в elif
            elif ((kto < 18) and (kto >12) or (grade_1 == 3)or(grade_2 == 3)or(grade_3 == 3)or(grade_4 == 3)or(grade_5 == 3)or(grade_6 == 3)):
                topl()
                btly_14['text'] = f"Имя: {zbty_1}\n Учебные данные: {zbty_2}\nКатегория: 2"
                btly_14['width'] = "21"
            elif (kto == 12):
                topl()
                btly_14['text'] = f"Имя: {zbty_1}\n Учебные данные: {zbty_2}\nКатегория: 3"
                btly_14['width'] = "21"
            else:
                topl()
                btly_14['text'] = f"Имя: {zbty_1}\n Учебные данные: {zbty_2}\nКатегория: 4"
                btly_14['width'] = "21"
    except:
        btly_14['text'] = "Ошибка, проверьте\nданные"
        btly_14['width'] = "20"
def cancellation():
    btly_3.config(state="normal")
    btly_4.config(state="normal")
    btly_3.delete(0, 'end')
    btly_4.delete(0, 'end')
    btly_14['text'] = "Результат будет вывиден \nпосле нажатия на кнопку \n(расчитать).\n\n Пожалуйста, введите\n оценки заново"
    
win = rtyp.Tk()
win.geometry("780x195+550+400")
win.overrideredirect(False) ## не исправлять!
#
btly_1 = rtyp.Label(win, text = "Введите свое имя: ")
btly_1.grid(row=0, column=0, padx = 5, pady = 5)
## введите пожалуйста только коротенькое число, после ввода большого кол-ва
## cимволов btly_14 будет кривой, все из за ограничений в функции при нажатии на btly_12
## виджеты я перенес в переменные для работы с их данными и параметрами
btly_2 = rtyp.Label(win, text = "Введите учебные данные: ") 
btly_2.grid(row=1, column=0, padx = 5, pady = 5)
#
btly_3 = rtyp.Entry(win, state="normal")
btly_3.grid(row=0, column=1, columnspan = 6, sticky = "we", padx = 5, pady = 5)
#
btly_4 = rtyp.Entry(win, state="normal")
btly_4.grid(row=1, column=1, columnspan = 6, sticky = "we", padx = 5, pady = 5)
#
btly_5 = rtyp.Label(win, text = "Задача №1")
btly_5.grid(row=3, column = 1, padx = 5, pady = 5)
## можно сделать рефакторинг, сокращение, перенос неизменяемых данных в функцию
grade_var_1 = rtyp.IntVar()
rtyp.Radiobutton(win, text = "0", variable = grade_var_1, value = 0, command = f_1rt).grid(row=4, column=1)
rtyp.Radiobutton(win, text = "1", variable = grade_var_1, value = 1, command = f_1rt).grid(row=5, column=1)
rtyp.Radiobutton(win, text = "2", variable = grade_var_1, value = 2, command = f_1rt).grid(row=6, column=1)
rtyp.Radiobutton(win, text = "3", variable = grade_var_1, value = 3, command = f_1rt).grid(row=7, column=1)
#
btly_6 = rtyp.Label(win, text = "Задача №2")
btly_6.grid(row=3, column=2, padx = 5, pady = 5)
#
grade_var_2 = rtyp.IntVar()
rtyp.Radiobutton(win, text = "0", variable = grade_var_2, value = 0, command = f_2rt).grid(row=4, column=2)
rtyp.Radiobutton(win, text = "1", variable = grade_var_2, value = 1, command = f_2rt).grid(row=5, column=2)
rtyp.Radiobutton(win, text = "2", variable = grade_var_2, value = 2, command = f_2rt).grid(row=6, column=2)
rtyp.Radiobutton(win, text = "3", variable = grade_var_2, value = 3, command = f_2rt).grid(row=7, column=2)
#
btly_7 = rtyp.Label(win, text = "Задача №3")
btly_7.grid(row=3, column=3, padx = 5, pady = 5)
#
grade_var_3 = rtyp.IntVar()
rtyp.Radiobutton(win, text = "0", variable = grade_var_3, value = 0, command = f_3rt).grid(row=4, column=3)
rtyp.Radiobutton(win, text = "1", variable = grade_var_3, value = 1, command = f_3rt).grid(row=5, column=3)
rtyp.Radiobutton(win, text = "2", variable = grade_var_3, value = 2, command = f_3rt).grid(row=6, column=3)
rtyp.Radiobutton(win, text = "3", variable = grade_var_3, value = 3, command = f_3rt).grid(row=7, column=3)
#
btly_8 = rtyp.Label(win, text = "Задача №4")
btly_8.grid(row=3, column=4, padx = 5, pady = 5)
#
grade_var_4 = rtyp.IntVar()
rtyp.Radiobutton(win, text = "0", variable = grade_var_4, value = 0, command = f_4rt).grid(row=4, column=4)
rtyp.Radiobutton(win, text = "1", variable = grade_var_4, value = 1, command = f_4rt).grid(row=5, column=4)
rtyp.Radiobutton(win, text = "2", variable = grade_var_4, value = 2, command = f_4rt).grid(row=6, column=4)
rtyp.Radiobutton(win, text = "3", variable = grade_var_4, value = 3, command = f_4rt).grid(row=7, column=4)
#
btly_9 = rtyp.Label(win, text = "Задача №5")
btly_9.grid(row=3, column=5, padx = 5, pady = 5)
#
grade_var_5 = rtyp.IntVar()
rtyp.Radiobutton(win, text = "0", variable = grade_var_5, value = 0, command = f_5rt).grid(row=4, column=5)
rtyp.Radiobutton(win, text = "1", variable = grade_var_5, value = 1, command = f_5rt).grid(row=5, column=5)
rtyp.Radiobutton(win, text = "2", variable = grade_var_5, value = 2, command = f_5rt).grid(row=6, column=5)
rtyp.Radiobutton(win, text = "3", variable = grade_var_5, value = 3, command = f_5rt).grid(row=7, column=5)
#
btly_10 = rtyp.Label(win, text = "Задача №6")
btly_10.grid(row=3, column=6, padx = 5, pady = 5)
#
grade_var_6 = rtyp.IntVar()
rtyp.Radiobutton(win, text = "0", variable = grade_var_6, value = 0, command = f_6rt).grid(row=4, column=6)
rtyp.Radiobutton(win, text = "1", variable = grade_var_6, value = 1, command = f_6rt).grid(row=5, column=6)
rtyp.Radiobutton(win, text = "2", variable = grade_var_6, value = 2, command = f_6rt).grid(row=6, column=6)
rtyp.Radiobutton(win, text = "3", variable = grade_var_6, value = 3, command = f_6rt).grid(row=7, column=6)
#
btly_11 = rtyp.Label(win, text = "Номер задачи: ")
btly_11.grid(row=3, column=0, padx = 5, pady = 5)
#
btly_12 = rtyp.Button(win, text = "Расчитать", command = conclusion)
btly_12.grid(row=4, column=0, rowspan=2, sticky = "nswe", padx = 5, pady = 5)
#
btly_13 = rtyp.Button(win, text = "Отмена", command = cancellation)
btly_13.grid(row=6, column=0, rowspan=2, sticky = "nswe", padx = 5, pady = 5)
#
btly_14 = rtyp.Label(win, text = "Результат будет вывиден \nпосле нажатия на кнопку \n(расчитать)", background="white")
btly_14.grid(row=0, column=8, rowspan=8, padx = 5, pady = 5, sticky = "nswe")
#
win.mainloop()







