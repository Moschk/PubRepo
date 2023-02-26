class Stack:                        #nome della classe (puo' essere qualsiasi ma si mette self)
    def __init__(self):                 #inizializza con se stessa come argomento che verra' nascosto durante la chiamata
        self.__stack_list = []              #assegna una lista privata__ con classe Stack al chiamante
                                            #DEFINISCE LA NATURA DELLA CLASSE


    def push(self, val):            #metodo per la classe che prende self(hide) e un val
        self.__stack_list.append(val)   #attacca val alla lista privata__


    def pop(self):                  #metodo per la classe che prende solo self(hide)
        val = self.__stack_list[-1]     #val prende l'ultimo valore della lista privata __
        del self.__stack_list[-1]       #toglie l'ultimo elemento della lista __privata
        return val                      #ritorna solo il val in maniera non privata

class AddingStack(Stack):           #crea una sottoclasse AddingStack di Stack
    def __init__(self):                 #inizializza con se stessa sull'argomento self
        Stack.__init__(self)                #inizializza sullo stesso argomento di Stack
        self.__sum = 0                      #crea la variabile privata__ sum = 0 DEF LA NATURA DEKKA SOTTOCLASSE

    def get_sum(self):              #crea il metodo su self(hide)
        return self.__sum               #ritorna il valore di __sum al chiamante

    def push(self, val):            #crea il metodo push per la sottoclasse che prende self(hide) e val
        self.__sum += val               #la variabile privata__ creata prima prende val in aggiunta
        Stack.push(self, val)           #usa il metodo push di Stack con val ()torna su e vedi cosa fa)

    def push(self, val):            #crea il metodo, passa self(h) e val
        self.__sum += val               #aumenta __sum (var privata) di val
        Stack.push(self, val)           #passa self(h) e val al metodo push di Stack (sopra)

    def pop(self):                  #crea il metodo pop che prende self(h)
        val = Stack.pop(self)           #val prende il valore del risultato di self(h) passato al metodo pop di Stack
        self.__sum -= val               #__sum (p) perde il valore di val
        return val                      #ritorna val al chiamante


stack_object = AddingStack()        #crea un oggetto della classe AddingStack

for i in range(5):                  
    stack_object.push(i)            #usa il metodo push di AddingStack(che usera' quello di Stack(vedi sopra)) con i (e self H)
print(stack_object.get_sum())       #stampa il valore di ritorno del metodo get_sum di AddingStack con nulla (self H)

for i in range(5):
    print(stack_object.pop())       #usa il metodo pop sull'oggetto senza passare valori (self H) e stampa il valore di ritorno
print('-'*30)


class QueueError(IndexError):       #crea una sottoclasse di IndexError
    pass                                #lascia proseguire il programma


class Queue:                        #crea una coda FIFO
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError
            print('BOOOOM!')

class SuperQueue(Queue):            #crea una sottoclasse di Queue estendendo il controllo dell'errore lista vuota
    def __init__(self):
        Queue.__init__(self)
        
    def isempty(self):
        return len(self.queue) == 0


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):                  #corpo che gestisce l'esaurimento della coda anche se ormai vuota
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")