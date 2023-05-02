with open("5_1.txt", encoding="utf-8") as f:
    lines = f.readlines()
    for i, line_1 in enumerate(lines):
        line_1 = line_1.split(" ")
        for line_2 in lines[i + 1:]:
            line_2 = line_2.split(" ")
            if line_2[1] == line_1[1]:
                if line_2[2].split("-")[0] == line_1[2].split("-")[0]:
                    print("есть")
                else:
                    print("Нет")



