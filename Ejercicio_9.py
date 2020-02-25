import math
xpun1=int(input("digite cordenada del primer punto "))
ypun1=int(input("digite cordenada del primer punto "))
xpun2=int(input("digite cordenada del segundo punto "))
ypun2=int(input("digite cordenada del segundo punto "))

print("la distancia entre los dos puntos es de: ",
      math.sqrt(abs(((xpun2*xpun1)*(xpun2-xpun1)+ ((ypun2-ypun1)*(ypun2-ypun1))))))
