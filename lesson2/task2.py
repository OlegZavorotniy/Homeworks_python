k = int(input("Введите количество индексов в список: "))
l = []
a = 0
while a < k:
    b = input("Введите любое число: ")
    l.append(b)
    a += 1
print(l)
c = 0
for i in range(int(len(l)/2)):
    l[c],l[c + 1] = l[c + 1],l[c]
    c +=2
print(l)
