#Сформувати функцію, що буде обчислювати факторіал заданого користувачем
#натурального числа n.
#Дудук Вадим
import sys
x=int(input('Введите число'))
def fact_rec(x):
    if x==1:
        return 1
    else:
       return fact_rec(x-1)*x
sys.setrecursionlimit(x+100)
print(fact_rec(x))
def fact_iter(x):
    count=1
    for i in range(1,x+1):
        count*=i
    print(count)
fact_iter(x)
#В даній задачі зручніше буде використовувати рекурсія,код став читабельніший і його легше реалізувати
