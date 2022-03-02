from Graphics.RectFunctions import*
from Graphics.SphFunctions import*
from Graphics.CirFunctions import*
l=int(input("enter l"))
b=int(input("enter b"))
print("area=",RectArea(l,b))
print("Perimeter=",RectPerimeter(l,b))
r=int(input("enter the radius of a circle"))
print("Circle area=",CirArea(r))
print("Circle perimeter=",Cirperimeter(r))
r=int(input("enter radius of sphere"))
print("Circle area=",SpArea(r))
print("Circle Perimeter=",SpPerimeter(r))
