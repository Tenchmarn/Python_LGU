import tkinter as rtyp
from tkinter import ttk


kto = 0

def topl():
    btly_3.config(state="readonly")
    btly_4.config(state="readonly")

   
def conclusion():
    global grade_1, grade_2, grade_3, grade_4, grade_5, grade_6
    grade_1 = int(YYY_1.get())
    grade_2 = int(YYY_2.get())
    grade_3 = int(YYY_3.get())
    grade_4 = int(YYY_4.get())
    grade_5 = int(YYY_5.get())
    grade_6 = int(YYY_6.get())
    try:
        global zbty_1, zbty_2, kto
        zbty_1 = btly_3.get()
        zbty_2 = btly_4.get()
        kto = grade_1 + grade_2 + grade_3 + grade_4 + grade_5 + grade_6
        if ((zbty_1 == '') and (zbty_2 == '')):
            btly_14['text'] = "Ошибка, недостаточно \n данных"
        else:
            if ((int(grade_1) == 3) and (grade_2 == 3) and (grade_3 == 3) and (grade_4 == 3) and (grade_5 == 3) and (grade_6 == 3)):
                topl()
                btly_14['text'] = f"Имя: {zbty_1}\n Учебные данные: {zbty_2}\nКатегория: 1"
                btly_14['width'] = "21"
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




    
rUlo = ("0", "1", "2", "3")





win = rtyp.Tk()
win.overrideredirect(False)

btly_1 = rtyp.Label(win, text = "Введите свое имя: ")
btly_1.grid(row=0, column=0, padx = 5, pady = 5)

btly_2 = rtyp.Label(win, text = "Введите учебные данные: ")
btly_2.grid(row=1, column=0, padx = 5, pady = 5)

btly_3 = rtyp.Entry(win, state="normal")
btly_3.grid(row=0, column=1, columnspan = 6, sticky = "we", padx = 5, pady = 5)

btly_4 = rtyp.Entry(win, state="normal")
btly_4.grid(row=1, column=1, columnspan = 6, sticky = "we", padx = 5, pady = 5)

btly_5 = rtyp.Label(win, text = "Задача №1")
btly_5.grid(row=3, column = 1)

YYY_1 = ttk.Combobox(win, values = rUlo)
YYY_1.grid(row=4, column=1)

btly_6 = rtyp.Label(win, text = "Задача №2")
btly_6.grid(row=3, column=2, padx = 5, pady = 5)

YYY_2 = ttk.Combobox(win, values = rUlo)
YYY_2.grid(row=4, column=2)

btly_7 = rtyp.Label(win, text = "Задача №3").grid(row=3, column=3, padx = 5, pady = 5)

YYY_3 = ttk.Combobox(win, values = rUlo)
YYY_3.grid(row=4, column=3)

btly_8 = rtyp.Label(win, text = "Задача №4").grid(row=3, column=4, padx = 5, pady = 5)

YYY_4 = ttk.Combobox(win, values = rUlo)
YYY_4.grid(row=4, column=4)

btly_9 = rtyp.Label(win, text = "Задача №5")
btly_9.grid(row=3, column=5, padx = 5, pady = 5)

YYY_5 = ttk.Combobox(win, values = rUlo)
YYY_5.grid(row=4, column=5)

btly_10 = rtyp.Label(win, text = "Задача №6")
btly_10.grid(row=3, column=6, padx = 5, pady = 5)

YYY_6 = ttk.Combobox(win, values = rUlo)
YYY_6.grid(row=4, column=6)

btly_11 = rtyp.Label(win, text = "Номер задачи: ")
btly_11.grid(row=3, column=0, padx = 5, pady = 5)

btly_12 = rtyp.Button(win, text = "Расчитать", command = conclusion)
btly_12.grid(row=4, column=0, rowspan=2, sticky = "nswe", padx = 5, pady = 5)

btly_13 = rtyp.Button(win, text = "Отмена", command = cancellation)
btly_13.grid(row=6, column=0, rowspan=2, sticky = "nswe", padx = 5, pady = 5)

btly_14 = rtyp.Label(win, text = "Результат будет вывиден \nпосле нажатия на кнопку \n(расчитать)", background="white")
btly_14.grid(row=0, column=8, rowspan=8, padx = 5, pady = 5, sticky = "nswe")

win.mainloop()



