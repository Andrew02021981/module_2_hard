import random
import time
def pool_1():
    list_ = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    n = random.choice(list_)
    return n
n = pool_1()
print('Случайное число от 3 до 20:',n)
time.sleep(2)
print('Терпение, мой друг! Еще секундочку)')
time.sleep(4)
sum_1 = 0
str_1 = ''
for j in range(1, n):
   for k in range(j, n):
       sum_1 = j + k
       if n % sum_1 == 0 and j != k:
            str_1 = str_1 + str(j) + str(k)

print ('Ваш пароль:',str_1)


