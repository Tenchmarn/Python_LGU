print(" Имя | Средний удельный вес")
with open("4_1.txt", encoding="utf-8") as f:
    for i in f.readlines():
        z = i.split(" ")
        if z[2].strip() == "3":
            print(z[0], float(z[1]) / 2)

