diccionario = {}
palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in palabras.split(','):
    key, value = i.split(':')
    diccionario[key] = value
fras = input('Introduce una frase en español: ')
for i in fras.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')

