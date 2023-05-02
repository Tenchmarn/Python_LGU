from datetime import datetime

winter = 0
spring = 0
summer = 0
autumn = 0

with open("3_1.txt") as f:
    for line in f.readlines():
        date = datetime.strptime(line.strip(), "%d.%m.%Y")
        if date.month == 12 or 1 <= date.month <= 2:
            winter += 1
        elif 3 <= date.month <= 5:
            spring += 1
        elif 6 <= date.month <= 8:
            summer += 1
        elif 9 <= date.month <= 11:
            autumn += 1

print(f"Зима: {winter}\nВесна: {spring}\nЛето: {summer}\nОсень: {autumn}")
