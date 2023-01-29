# Calculate the simmetric difference between any number of sets, recursively (associativa a sinistra), no repetitions
# return a list

def simmetric_diff(*args):
    set_diff = []
    #base case
    if len(args) == 2:
        set1 = args[0]
        set2 = args[1]
        for i in range(len(set1)):
            if (set1[i] not in set2 and set1[i] not in set_diff ):
                set_diff.append(set1[i])
        for i in range(len(set2)):
            if (set2[i] not in set1 and set2[i] not in set_diff ):
                set_diff.append(set2[i])
        return set_diff
    #recusion
    else:
        return simmetric_diff( simmetric_diff(*(args[0:-1])), args[-1] )


# TEST 1
# set1 = (1,2,2,3)
# set2 = (1,3,4,4)
# set3 = (4,5,5,7)
# print(simmetric_diff(set1, set2, set3))

# TEST 2
# t = sorted(simmetric_diff([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]))
# assert t == [1, 2, 4, 5, 6, 7, 8, 9]
# print(simmetric_diff([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]))

# TEST 3
# print(simmetric_diff('asdqwer', 'asderytdf', 'lkjpow', 'kjhgjhfee'))
