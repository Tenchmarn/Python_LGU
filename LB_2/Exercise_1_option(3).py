import tkinter as rtyp

kto = 0

def topl():
    btly_3.config(state="readonly")
    btly_4.config(state="readonly")
    
## по условию задания, нужно определить только группу по оценкам,
## переменные zbty_1 и zbty_2 не редактировал, только вывел

def conclusion():
    global grade_1, grade_2, grade_3, grade_4, grade_5, grade_6, item_1, item_2, item_3, item_4, item_5, item_6
    grade_1 = list(thpo_1.curselection())
    item_1 = grade_1.pop(0)
    print(f"значение списка №1: {item_1}")





#### 
    grade_2 = list(thpo_2.curselection())
    item_2 = grade_2.pop(0)
    print(f"значение списка №2: {item_2}")
#######


    
    grade_3 = list(thpo_3.curselection())
    item_3 = grade_3.pop(0)
    print(f"значение списка №3: {item_3}")
    grade_4 = list(thpo_4.curselection())
    item_4 = grade_4.pop(0)
    print(f"значение списка №4: {item_4}")
    grade_5 = list(thpo_5.curselection())
    item_5 = grade_5.pop(0)
    print(f"значение списка №5: {item_5}")
    grade_6 = list(thpo_6.curselection())
    item_6 = grade_6.pop(0)
    print(f"значение списка №6: {item_6}")
    try:
        global zbty_1, zbty_2, kto
        zbty_1 = btly_3.get()
        zbty_2 = btly_4.get()
        kto = item_1 + item_2 + item_3 + item_4 + item_5 + item_6
        if ((zbty_1 == '') and (zbty_2 == '')):
            btly_14['text'] = "Ошибка, недостаточно \n данных"
        else:
            if ((item_1 == 3) and (item_2 == 3) and (item_3 == 3) and (item_4 == 3) and (item_5 == 3) and (item_6 == 3)):
                topl()
                btly_14['text'] = f"Имя: {zbty_1}\n Учебные данные: {zbty_2}\nКатегория: 1"
                btly_14['width'] = "21"
            elif ((kto < 18) and (kto >12) or (item_1 == 3)or(item_2 == 3)or(item_3 == 3)or(item_4 == 3)or(item_5 == 3)or(item_6 == 3)):
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
##win.geometry("780x195+550+400")
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







btly_5 = rtyp.Label(win, text = "Задача №1")
btly_5.grid(row=3, column = 1, padx = 5, pady = 5)

pfx_1 = ["3", "2", "1", "0"]
thpo_1 = rtyp.Listbox(win, exportselection=0)
for i in pfx_1:
    thpo_1.insert(0, i)
thpo_1.grid(row=4, column=1, pady = 5, padx = 5)




























############
btly_6 = rtyp.Label(win, text = "Задача №2")
btly_6.grid(row=3, column=2, padx = 5, pady = 5)


pfx_2 = ["3", "2", "1", "0"]
thpo_2 = rtyp.Listbox(win, exportselection=0)
for i in pfx_2:
    thpo_2.insert(0, i)
thpo_2.grid(row=4, column=2, pady = 5, padx = 5)
##################

















btly_7 = rtyp.Label(win, text = "Задача №3")
btly_7.grid(row=3, column=3, padx = 5, pady = 5)
pfx_3 = ["3", "2", "1", "0"]
thpo_3 = rtyp.Listbox(win, exportselection=0)
for i in pfx_3:
    thpo_3.insert(0, i)
thpo_3.grid(row=4, column=3, pady = 5, padx = 5)

btly_8 = rtyp.Label(win, text = "Задача №4")
btly_8.grid(row=3, column=4, padx = 5, pady = 5)
pfx_4 = ["3", "2", "1", "0"]
thpo_4 = rtyp.Listbox(win, exportselection=0)
for i in pfx_4:
    thpo_4.insert(0, i)
thpo_4.grid(row=4, column=4, pady = 5, padx = 5)

btly_9 = rtyp.Label(win, text = "Задача №5")
btly_9.grid(row=3, column=5, padx = 5, pady = 5)
pfx_5 = ["3", "2", "1", "0"]
thpo_5 = rtyp.Listbox(win, exportselection=0)
for i in pfx_5:
    thpo_5.insert(0, i)
thpo_5.grid(row=4, column=5, pady = 5, padx = 5)

btly_10 = rtyp.Label(win, text = "Задача №6")
btly_10.grid(row=3, column=6, padx = 5, pady = 5)
pfx_6 = ["3", "2", "1", "0"]
thpo_6 = rtyp.Listbox(win, exportselection=0)
for i in pfx_6:
    thpo_6.insert(0, i)
thpo_6.grid(row=4, column=6, pady = 5, padx = 5)

btly_11 = rtyp.Label(win, text = "Номер задачи: ")
btly_11.grid(row=3, column=0, padx = 5, pady = 5)
#
btly_12 = rtyp.Button(win, text = "Расчитать", command = conclusion)
btly_12.grid(row=4, column=0, rowspan=2, sticky = "nswe", padx = 5, pady = 5)
#
btly_13 = rtyp.Button(win, text = "Отмена", command = cancellation)
btly_13.grid(row=6, column=0, sticky = "nswe", padx = 5, pady = 5, columnspan=7)
#
btly_14 = rtyp.Label(win, text = "Результат будет вывиден \nпосле нажатия на кнопку \n(расчитать)", background="white")
btly_14.grid(row=0, column=8, rowspan=8, padx = 5, pady = 5, sticky = "nswe")
#
win.mainloop()







