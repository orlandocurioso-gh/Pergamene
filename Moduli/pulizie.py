def cancellaTestaLista(lista):
        for i in range(4):
            lista.pop(0)
        return lista

def pulisciFileFinale(lista):
    for elemento in lista:
        if 'nat' in elemento:
            match elemento:
                case 'nata a':
                    lista.append('f')
                case 'nato a':
                    lista.append('m')
            lista.remove(elemento)
    return lista

def controlloProvincia(lista):
    if '(' not in lista[4]:
        provincia='('+lista[3]+')'
        lista.insert(4,provincia)
    return lista

def controlloAbilitazione(lista):
    if 'Abilitante' not in lista[6]:
        lista.insert(6,'')
    return lista

def controlloClasseLaurea(lista):
    if 'Classe' not in lista[7]:
        lista.insert(7,'')
    return lista

def controlloLode(lista):
    if 'Lode' not in lista[8]:
        lista.insert(8,'')
    return lista