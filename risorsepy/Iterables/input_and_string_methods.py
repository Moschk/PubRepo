import fileinput

# carica gli input una line alla volta
x=[]
for line in fileinput.input(files="risorsepy/input.txt"):
    x.append(line)
print(x)

# carica una linea alla volta senza il carattere new line
x=[]
for line in fileinput.input(files="risorsepy/input.txt"):
    x.append(line.removesuffix('\n'))

print(x)

# carica una linea spezzandola alla prima occorrenza di un char specifico
# .partition crea una TUPLA di 3 elementi
# Ex( ('ciao nonna'), (','), ('77') )
x=[]
for line in fileinput.input(files="risorsepy/input.txt"):
    temp = []
    temp = list( (line.removesuffix('\n') ).partition(','))
    del temp[1]
    x.append(temp)
print(x)

