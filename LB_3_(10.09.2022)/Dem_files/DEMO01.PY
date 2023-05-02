f = open('numbers.txt', 'w')
s=""
print("Создание файла.\n")
print("Задайте количество элементов в файле:\n")
n=int(input())
for i in range(0,n,1):
 print("Введите элемент файла:\n")
 s=str(input(""))
 f.write(s)
 f.write("\n")
f.close
print("В файл были записаны данные:\n")
f = open('numbers.txt', 'r+')
s=''
st=f.readline()
for i in range(0,len(st)-1,1):
   s=s+st[i]
print(s)   
while not(st==''):
  s='' 
  st=f.readline()
  for i in range(0,len(st)-1,1):
   s=s+st[i]
  print(s)
f.close
