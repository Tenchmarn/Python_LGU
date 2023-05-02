print("В файл записаны данные:\n")
f = open('numbers.txt', 'r+')
s=''
st=f.readline()
for i in range(0,len(st)-1,1):
   s=s+st[i]
s=s+' '   
while not(st==''):
  st=f.readline()
  for i in range(0,len(st)-1,1):
    s=s+st[i]
  s=s+' '
print(s)
f.close
