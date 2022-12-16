import tkinter as artn
cent=0
value_1=0
value_2=0
value_0=0
def calculation():
    global value_0
    global cent
    try:
        value_1 = int(btny_3.get())
        value_2 = int(btny_4.get())
        value_0 = value_2 / value_1
        cent = value_0 - int(value_0)
        if (value_0<=0):
            btny_3.delete(0, 'end')
            btny_4.delete(0, 'end')
            btny_7['text'] = "Пожалуйста, введите \nдругое значение"
        else:
            btny_7['text'] = "Вы сможете \n купить {int(round(value_0, 0))} ($) и \n {int(round(cent, 2)*100)} цента(ов)"
            btny_3['state'] = "readonly"
            btny_4['state'] = "readonly"
    except:
        btny_3.delete(0, 'end')
        btny_4.delete(0, 'end')
        btny_7['text'] = "Ошибка символа, \nвведите число!"
        
def cancellation():
    btny_3['state'] = "normal"
    btny_4['state'] = "normal"
    btny_3.delete(0, 'end')
    btny_4.delete(0, 'end')
    value_0=0
    btny_7['text'] = "Нажмите (расчет)\n для расчета"


win = artn.Tk()
win.title('Задание_2')
win.resizable(False, False)


btny_1 = artn.Label(win, text = "Курс валюты ($): ")  
btny_1.grid(row=0, column=0, pady=5, padx=5)

btny_2 = artn.Label(win, text = "Введите имеющуюся \n сумму в рублях:")
btny_2.grid(row=1, column=0, pady=5, padx=5) 

btny_3 = artn.Entry(win)
btny_3.grid(row=0, column=1, pady=5, padx=5) 

btny_4 = artn.Entry(win)
btny_4.grid(row=1, column=1, pady=5, padx=5) 

btny_5 = artn.Button(win, text = "Расчитать", command = calculation)
btny_5.grid(row=2, column=0, sticky="we", pady=5, padx=5)  

btny_6 = artn.Button(win, text = "Отмена", command = cancellation)
btny_6.grid(row=3, column=0, sticky="we", pady=5, padx=5)  

btny_7 = artn.Label(win, text = "Нажмите (расчет)\n для расчета" ) 
btny_7.grid(row=2, column=1, rowspan=2, pady=5, padx=5)

win.mainloop() 
