from tkinter import messagebox
import tkinter as rypi
import math

a = ostatok = vion_0 = vion_1 = 0

## 1 доллар это 60 рублей, т.е. 1 = 60          (07.09.2022)
## 1 рубль это 0,016 доллара, т.е. 1 = 0,016    (07.09.2022)

def ylo():
    tbln_3.config(state="readonly")
    tbln_4.config(state="readonly")

def rtQw():
    tbln_3['state'] = "normal"
    tbln_3.delete(0, 'end')
    tbln_4['state'] = "normal"
    tbln_4.delete(0, 'end')
    tbln_6['text'] = "введите значения и \nнажмите (расчитать)\n для расчета"

def G_2tyr():
    global BCA_2, vion_1
    vion_1 = BCA_2.get()

def ttyu():
    global value_1, value_2, value_0, ostatok
    if (vion_1==1):
        value_1 = float(tbln_3.get())
        value_2 = float(tbln_4.get())
        value_0 = value_2 / value_1
        a = value_0 / 10
        value_0-=a
        ostatok = value_0 - int(value_0)
        ylo()
    else:
        value_1 = float(tbln_3.get())
        value_2 = float(tbln_4.get())
        value_0 = value_2 / value_1
        ostatok = value_0 - int(value_0)
        ylo()

def G_1tyr():
    global BCA_1, vion_0
    vion_0 = BCA_1.get()
    if (vion_0 == 0):
        C_1['text'] = "Купить рубли"
        tbln_1['text'] = "Укажите курс валюты ($): "
        tbln_2['text'] = "Укажите вашу сумму (Р): "
        rtQw()
    else:
        C_1['text'] = "Купить доллары"
        tbln_1['text'] = "Укажите курс валюты (Р): "
        tbln_2['text'] = "Укажите вашу сумму ($): "
        rtQw()

def calculation():
    try:
        global value_0, value_1, value_2
        global cent
        if (vion_0 == 1):
            ttyu()
            if (value_0<=0):
                tbln_3.delete(0, 'end')
                tbln_4.delete(0, 'end')
                tbln_6['text'] = "Пожалуйста, введите \nдругое значение"
            else:
                tbln_6['text'] = f"Вы можете купить\n{int(round(math.floor(value_0), 0))} (Р) рублей\n и {int(round(ostatok, 2)*100)} копеек"
        else:
            tbln_1['text'] = "Укажите курс валюты ($): "
            tbln_2['text'] = "Укажите вашу сумму (Р): "
            ttyu()
            if (value_0<=0):
                tbln_3.delete(0, 'end')
                tbln_4.delete(0, 'end')
                tbln_6['text'] = "Пожалуйста, введите \nдругое значение"
            else:
                tbln_6['text'] = f"Вы можете купить\n{int(round(math.floor(value_0), 0))} ($) долларов\n и {int(round(ostatok, 2)*100)} цента(ов)" 
    except:
        tbln_3.delete(0, 'end')
        tbln_4.delete(0, 'end')
        messagebox.showinfo('Внимание', 'Ошибка, введите пожалуйста числа')


def cancellation ():
    tbln_3['state'] = "normal"
    tbln_4['state'] = "normal"
    tbln_3.delete(0, 'end')
    tbln_4.delete(0, 'end')
    tbln_6['text'] = "введите значения и \nнажмите (расчитать)\n для расчета"
    
win = rypi.Tk()




BCA_1 = rypi.IntVar()
C_1 = rypi.Checkbutton(win, text = "Купить рубли", variable=BCA_1, command = G_1tyr)
C_1.grid(row=0, column=0, padx=3, pady=3)

BCA_2 = rypi.IntVar()
C_2 = rypi.Checkbutton(win, text = "Комиссия", variable = BCA_2, command = G_2tyr)
C_2.grid(row=0, column=1, padx=3, pady=3)

tbln_1 = rypi.Label(win, text = "Укажите курс валюты ($): ") 
tbln_1.grid(row=1, column=0, padx=5, pady=5, sticky = "swne")

tbln_2 = rypi.Label(win, text = "Укажите вашу сумму (Р): ")
tbln_2.grid(row=2, column=0, padx=5, pady=5, sticky = "swne")

tbln_3 = rypi.Entry(win)
tbln_3.grid(row=1, column=1, padx=5, pady=5)

tbln_4 = rypi.Entry(win)
tbln_4.grid(row=2, column=1, padx=5, pady=5)

tbln_5 = rypi.Button(win, text = "Расчитать", command = calculation)
tbln_5.grid(row=3, column=0, padx=5, pady=5, sticky = "swne")

tbln_5 = rypi.Button(win, text = "Отмена", command = cancellation)
tbln_5.grid(row=4, column=0, padx=5, pady=5, sticky = "swne")

tbln_6 = rypi.Label(win, text = "введите значения и \nнажмите (расчитать)\n для расчета")
tbln_6.grid(row=3, column=1, rowspan=2, padx=5, pady=5)

win.mainloop()
