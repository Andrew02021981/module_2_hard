n = int(input('Введите целое число от 3 до 20: '))
list_1 = []
sum_1 = 0
str_1 = ''
for i in range(0, n):
    list_1.append(i)
for j in range(1, n):
   for k in range(j, n):
       sum_1 = list_1[j] + list_1[k]
       if n % sum_1 == 0 and j != k:
            str_1 = str_1 + str(j) + str(k)

print (str_1)

