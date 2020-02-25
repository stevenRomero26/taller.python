clientes = {}
op = ''
while op != '6':
    if op == '1':
        nif = input('Introduce NIF del cliente: ')
        nombress = input('Introduce el nombre del cliente: ')
        dir = input('Introduce la dirección del cliente: ')
        telf = input('Introduce el teléfono del cliente: ')
        email = input('Introduce el correo electrónico del cliente: ')
        vip = input('¿Es un cliente preferente (S/N)? ')
        client = {'nombre':nombress, 'dirección':dir, 'teléfono':telf, 'email':email, 'preferente':vip=='S'}
        clientes[nif] = client
    if op == '2':
        nif = input('Introduce NIF del cliente: ')
        if nif in clientes:
            del clientes[nif]
        else:
            print('No existe el cliente con el nif', nif)
    if op == '3':
        nif = input('Introduce NIF del cliente: ')
        if nif in clientes:
            print('NIF:', nif)
            for key, value in clientes[nif].items():
                print(key.title() + ':', value)
        else:
            print('No existe el cliente con el nif', nif)
    if op == '4':
        print('Lista de clientes')
        for key, value in clientes.items():
            print(key, value['nombre'])
    if op == '5':
        print('Lista de clientes preferentes')
        for key, value in clientes.items():
            if value['preferente']:
                print(key, value['nombre'])
    op = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')
