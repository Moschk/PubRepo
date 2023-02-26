#creiamo un for per fare una lista con N coppie
N = 20
listacoppie = []
interrompipag = '----------------------------------------'
for i in range(N):
    listacoppie.append( (i, N-i) )
#e crea una funzione per stamparlo in maniera ordinata in righe di 5 coppie
def stampa_lista(l):
    for i in range(len(l)):
        if (i+1) % 5 == 0:
            print(l[i], '\n')
        else: print(l[i], end='')
    print(interrompipag)

#crea una tupla basata sulla lista di base
tupla_base = tuple(listacoppie)
#e crea una funzione per stamparlo in righe da 5
def stampa_tupla(t):
    for i in range(len(t)):
        if (i+1) % 5 == 0:
            print(t[i], '\n')
        else: print(t[i], end='')
    print(interrompipag)

#crea un dizionario basato sulla lista base
dict_base = dict(listacoppie)
#e crea una funzione per stamparlo in righe da 4
def stampa_dict(d):
    count = 1
    for k,v in d.items():
        if count % 4 == 0:
            print('{k ',k, ': v ',v, '} ', '\n')
        else: print('{k ',k, ': v ',v, '} ', end='')
        count += 1
    print(interrompipag)

#stampa tutto il preparato finora
stampa_lista(listacoppie)
stampa_tupla(tupla_base)
stampa_dict(dict_base)
print(interrompipag)

#allenati ora cambiando e stampando i risultati
tupla_base = list(tupla_base)
del tupla_base[4]
tupla_base = tuple(tupla_base)
stampa_tupla(tupla_base)


