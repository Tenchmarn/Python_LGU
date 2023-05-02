import tkinter as df
file_0 = open('1_1.txt').read().split()
lst = []
def gf():
    for i in file_0:
        if i.isdigit():
            lst.append(int(i))
            sum(lst)   
    df.Label(win, text = f"Ответ: {sum(lst)}").pack()

win = df.Tk()
btn_1 = df.Button(win, text = "нажмите на меня", command = gf).pack()
win.mainloop()





