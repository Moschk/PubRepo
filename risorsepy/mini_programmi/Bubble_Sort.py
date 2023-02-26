my_list = []
swapped = True

#Inserimento di N elementi decisi a priori dall'utente
#num = int(input("How many elements do you want to sort: "))

#for i in range(num):
#    val = float(input("Enter a list element: "))
#    my_list.append(val)


#Inserimento fino a 10 elementi da riordinare
my_list.append(float(input("Insert a number: ")))
temp = 0

while True:
    temp = input("Insert a number or S for sorting: ")
    if temp == 'S' or len(my_list) == 9:
        break
    else:
        my_list.append(float(temp))
    
        
#BUBBLE SORT
while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nBubble Sorted:")
print(my_list)


