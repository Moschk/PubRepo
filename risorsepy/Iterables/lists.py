#in, not in operators per il controllo della presenza di elementi nelle liste
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

listnorep = [my_list[0]]
print(listnorep)


for i in my_list:
    if i not in listnorep:
        listnorep.append(i)

print("The list with unique elements only:", listnorep, '\n')


#versione estesa della creazione di liste con ciclo for
row = []
for i in range(10):
    row.append(i ** 2)
print(row)


#versione compatta della creazione di liste 
#list comprehension
squares = [x ** 2 for x in range(10)]
print(squares)

#variante con condizione
odds = [x for x in squares if x % 2 != 0 ]
print(odds)


#SORTING

#sorted(list)   funzione che lascia invariata la lista argomento
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)
print(first_greek)
print(first_greek_2)

#list.sort()    metodo che trasforma la lista input
second_greek = ['omega', 'alpha', 'pi', 'gamma']
second_greek.sort()
print(second_greek)