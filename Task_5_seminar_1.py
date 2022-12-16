# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними 
# в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = int(input("Input coordinate x1: "))
y1 = int(input("Input coordinate y1: "))
x2 = int(input("Input coordinate x2: "))
y2 = int(input("Input coordinate y2: "))



def Lenght(a1, b1, a2, b2):
    length = ((a2-a1)**2 + (b2-b1)**2)**(1/2)
    return length

x = round(Lenght(x1,y1,x2,y2),2)
print(f"A({x1};{y1}); B({x2};{y2})  -->  {x}")



   



