
prices=[]
for x in range(9):
    valor=int(input("Ingrese un valor entero:"))
    prices.append(valor)

suma=0
max = prices[0]

laSuma = 0
for price in prices:
    laSuma = laSuma + price

     
   

    
    if price > max:
        max = price
promedio=laSuma/9     

print("El máximo es " + str(max))
print("cantidad de veces numero (5) ",prices.count(5))
print("el promedio de los numeros es: ", promedio);

        
   



