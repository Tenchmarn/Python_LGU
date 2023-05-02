numbers = list(map(int, input().split()))
with open("2_1.txt", "w") as f:
    for i in range(len(numbers)):
        if (i + 1) % 2 == 0 and numbers[i] % 2 == 0:
            f.write(f"{numbers[i] / 2}\n")
        else:
            f.write(f"{numbers[i]}\n")


