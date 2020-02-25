

g29=int(input("digite cantidad de personas"))
promedio_imc=0
for e in range(g29):
    e=e+1
    print("persona",e)
    peso = float (input("digite su peso :"))
    altura =  float (input  ("digite su altura :"))
    
    IMC=peso/altura**2
    promedio_imc+=IMC/g29
print("el promedio es =",promedio_imc)
if(promedio_imc<=15):
  print("promedio delgadex muy severa")
elif(promedio_imc==15 or promedio_imc==15.9):
        print("delgades severa")

