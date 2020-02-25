frutas = {'Plátano':1.35, 'ManzanaVerde':0.8, 'Pera':0.85, 'melon':0.7}
f = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if f in frutas:
    print(kg, 'kilos de', f, 'valen', frutas[f]*kg )
else: 
    print("Lo siento, la fruta", f, "no está disponible.")
