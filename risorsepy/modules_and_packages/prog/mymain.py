#!/usr/bin/env python3
import mymodule1
from pprint import pprint
from sys import path

n = 3
print()

print(__name__)

pprint(path)
print( '\n', '*'*30)
path.append('risorsepy\\modules_and_packages\\modules_example')# path relativo per mymodule 2
path.append('risorsepy\\modules_and_packages\\modules_example\\modules')# path relativo per mymodule 3
#path.append('C:\\Users\\dermo\\Documents\\Python\\risorsepy\\modules_and_packages\\modules_example\\modules')
#NON INDICARE IL FILE MA LA CARTELLA DOVE E' CONTENUTO IL FILE!!
#doppia \ perche' la prima la ignora
pprint(path)
import mymodule2, mymodule3



print(mymodule1.funterza(n))
print(mymodule1.funterza(n))
print(mymodule2.funseconda(mymodule2.funseconda(n)))
print(mymodule1.funterza(n), mymodule1.counter)
print(mymodule3.fun1terzo(n), mymodule1.counter)