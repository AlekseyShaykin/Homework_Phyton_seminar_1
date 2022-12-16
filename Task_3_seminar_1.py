# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка .
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def InputCoordX():
    x = int(input("Input coordinate X: "))
    return x

def InputCoordY():
    y = int(input("Input coordinate Y: "))
    return y

def Definition(a,b):
    if a>0 and b>0:
        print("Четверть №1")
    elif a<0 and b>0:
        print("Четверть №2")
    elif a<0 and b<0:
        print("Четверть №3")
    elif a>0 and b<0:
        print("Четверть №4")


def Check(k,l):
    if k!=0 and l!=0:
        Definition(k,l)
    else:
        print("Введите координаты неравные 0")
        k = InputCoordX()
        l = InputCoordY()
        Check(k,l)

x = InputCoordX()
y = InputCoordY()
Check(x,y)
