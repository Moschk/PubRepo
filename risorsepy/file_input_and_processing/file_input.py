# A text file contains some text (nothing unusual) but we need to know how often (or how rare) each letter appears in the text.
# Such an analysis may be useful in cryptography, so we want to be able to do that in reference to the Latin alphabet.

# Your task is to write a program which:

# asks the user for the input file's name;
# reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
# prints a simple histogram in alphabetical order (only non-zero counts should be presented)
# Create a test file for the code, and check if your histogram contains valid results.

# Your task is to make some amendments, which generate the following results:

# the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
# the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist'
# (it should be concatenated to the original name)

from os import strerror

dict_occ = dict([ (chr(n), 0) for n in range(ord('a'),ord('z')+1) ])

try:
    file_name = input('Name file: ')
    file = open(file_name, 'rt') # A new file (newtext.txt) is created.
    for line in file:
        line = line.lower()
        for char in line:
            if char.isalpha():
                if char in dict_occ:
                    dict_occ[char] += 1
        print()
    file.close()

    file = open(file_name + '.hist', 'wt')#crea il file vuoto
    # Note: we've used a lambda to access the directory's elements and set reverse to get a valid order.
    for char in sorted(dict_occ.keys(), key=lambda x: dict_occ[x], reverse=True):
        c = dict_occ[char]
        if c > 0:
            file.write(char + ' -> ' + str(c) + '\n')#scrive nel file creato
    file.close()

    # for char in counters.keys():
    #     c = counters[char]
    #     if c > 0:
    #         print(char, '->', c)
    # temp = []
    # for occ in dict_occ:
    #     if dict_occ[occ] > 0:
    #         temp.append( [dict_occ[occ], occ] )
    # temp.sort(reverse=True)
    # print(temp)
    # for t in temp:
    #     print(t[1], ' -> ', t[0])

except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))

## HTML file creation and open it with browser

import webbrowser
#hmtl string to copy
html_s = '<h1>CIAO POVERY!</h1>'

stream = open('prova.html', 'w')
stream.write(html_s)
stream.close()

url = 'prova.html'
webbrowser.open_new_tab(url)    