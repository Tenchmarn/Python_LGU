from tkinter import messagebox
import tkinter as VoUty
import math

vbh=0
summa_produktov = 0
summa_skidki = 0
kopeiki = 0

def gf():
    global select, item, vbh, summa_produktov, summa_skidki, kopeiki, a
    try:
        select = list(thpo_1.curselection())
        item = select.pop(0)
        jhn()
        if (vbh == 1):
            print('Скидка есть')
            if (int(item) == 0): ## 65
                summa_produktov = summa_produktov + 65
            elif (item == 1): ## 23
                summa_produktov = summa_produktov + 23
            elif (item == 2): ## 78
                summa_produktov = summa_produktov + 78
            elif (item == 3): ## 232
                summa_produktov = summa_produktov + 232
            elif (item == 4): ## 678
                summa_produktov = summa_produktov + 678
            elif (item == 5): ## 23
                summa_produktov = summa_produktov + 23
            else:
                print('ошибка')
            float(summa_produktov)
            summa_skidki = float((3 *(summa_produktov / 100)))
            summa_produktov = summa_produktov - (3 *(summa_produktov / 100))
            kopeiki = summa_skidki - int(summa_skidki)
            print(summa_skidki)
            print(kopeiki)
            thpo_0['text'] = f"Сумма товаров: {round(summa_produktov, 0)} рублей"
            thpo_3['text'] = f"Общая скидка: {int(round(math.floor(summa_skidki), 0))} рублей \n и  {int(round((kopeiki*100),0))} копеек(йки) \n C учетом скидки"
        else:
            print("скидки пока нет")
            if (int(item) == 0): ## 65
                summa_produktov = summa_produktov + 65
            elif (item == 1): ## 23
                summa_produktov = summa_produktov + 23
            elif (item == 2): ## 78
                summa_produktov = summa_produktov + 78
            elif (item == 3): ## 232
                summa_produktov = summa_produktov + 232
            elif (item == 4): ## 678
                summa_produktov = summa_produktov + 678
            elif (item == 5): ## 23
                summa_produktov = summa_produktov + 23
            else:
                print('ошибка')    
            thpo_0['text'] = f"{round(summa_produktov, 0)} рублей"
    except:
        messagebox.showinfo('Упсс...', 'Возможно вы ничего не выбрали, повторите попытку!')

def jhn():
    global BCA_0, vbh
    vbh = int(BCA_0.get())
        

win = VoUty.Tk()
##win.geometry("300x365+350+50") ##140x320



## поле вывода стоимости выборов
thpo_0 = VoUty.Label(win, text = "Тут будет общая сумма товаров")
thpo_0.grid(row=0, column=0, pady = 3, padx = 8)

## поле (список) имеющихся товаров
pfx = ["Молоко", "Шоколад", "Сыр", "Печенье", "Пирожное", "Огурчики"]
thpo_1 = VoUty.Listbox(win)
for i in pfx:
    thpo_1.insert(0, i)
thpo_1.grid(row=3, column=0, pady = 3, padx = 8)


## поле именования навигации к thpo_1
thpo_2 = VoUty.Button(win, text = "Выберите товар\nниже, после \nнажмите сюда", command = gf)
thpo_2.grid(row=2, column=0, pady = 3, padx = 5)


## бокс бля обозначения наличия карты у покупателей, если есть то скидка -3%
BCA_0 = VoUty.IntVar()
thpo_3 = VoUty.Checkbutton(win, text = "Скидочная карта ", variable=BCA_0, command = jhn)
thpo_3.grid(row=4, column=0, pady = 3, padx = 8)

thpo_3 = VoUty.Label(win, text = "Без учета скадки")
thpo_3.grid(row=1, column = 0, pady = 3, padx = 8)

win.mainloop()
