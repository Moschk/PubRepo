#creazione di liste di liste
#ovvero matrici
#ovvero two dimensional arrays

#crea una lista di i(8) elementi 'EMPTY' e la usa come elemento per ogni j(8) elemento della lista board
board = [['EMPTY' for i in range(8)] for j in range(8)]
print(board)

#crea 4 liste di numeri da 1 a 4, le inserisce in una lista di 4 elementi
board = [ [(1 + i) for i in range(4)] for j in range(4)]
print(board)#stampa la lista di liste creata
print(board[0][1])#stampa il secondo elemento della prima lista

#crea una lista di 3 liste di 4 liste con liste di 5 elementi False
#brematurata come un spazio 3d con scappellamento a destra, se fosse
#un hotel con 3 pianie 4 stanze da 5 posti del cognato del vicesindaco
rooms = [[[False for r in range(5)] for f in range(4)] for t in range(3)]
for i in range(3): print(rooms[i],'\n')
