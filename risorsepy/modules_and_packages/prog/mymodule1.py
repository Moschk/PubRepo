#!/usr/bin/env python3
# dice al SO basato su Unix dove deve eseguire il programma
# inutile su Windows
# may be called shabang, shebang, hashbang, poundbang or even hashpling 

# doc string
# piazzata all'inizio per descrivere il contenuto del documento(modulo)

counter = 0

def funterza(n):
    global counter
    print(__name__)
    counter += 1
    return (n**3, counter)

print(__name__)