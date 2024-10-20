n = int(input('Введите целое число от 3 до 20: '))
list_1 = []
list_2 = []
sum_1 = 0
str_1 = ''
for i in range(0, n):
    list_1.append(i)
for j in range(1, n):
    for k in range(2, n):
        sum_1 = list_1[j] + list_1[k]
        if n % sum_1 == 0 and j != k:
            #list_2.append(j)
            #list_2.append(k)
            str_1 = str_1 + str(j) + str(k)


print (str_1)

