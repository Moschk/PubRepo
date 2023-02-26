'''
Python strings can be compared using the same set of operators which are in use in relation to numbers.
==, !=, >, >=, <, <=
It compares code point values, character by character

The final relation between strings is determined by comparing the first different character in both strings
(keep ASCII/UNICODE code points in mind at all times.)

When you compare two strings of different lengths and the shorter one is identical to the beginning of the
longer one, the longer string is considered greater.

COMPARISON BETWEEN STRING AND INT
The only comparisons you can perform with impunity are these symbolized by the == and != operators.
The former always gives False, while the latter always produces True.
Using any of the remaining comparison operators will raise a TypeError exception.

'''

#capitalize()
#creates a new string filled with characters taken from the source string
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())


#center()
#makes a copy of the original string, trying to center it inside a field of a specified width
print('[' + 'alpha'.center(10) + ']')#--->[  alpha   ]
print('[' + 'gamma'.center(20, '*') + ']')#--->[*******gamma********]


#endswith()
#startswith()
#checks if the given string ends with the specified argument and returns True or False
t = "zeta"
print(t.endswith("a"))#True
print(t.endswith("A"))#False
print(t.endswith("et"))#False
print(t.endswith("eta"))#True


#find() #strings only
#looks for a substring and returns the index of the first occurrence of this substring
print("Eta".find("ta"))#--->1
print("Eta".find("mma"))#--->-1 SE NON TROVA!
#specifies the index at which the search will be started
print('kappa'.find('a', 2))#--->4
#the third argument points to the first index which won't be taken into consideration during the search
print('kappa'.find('a', 1, 4))#--->1
print('kappa'.find('a', 2, 4))#--->-1


#check if
#isalnum() alphanumeric
#isalpha() letter case only
#isdigit() digits only
#islower() lower-case letters only
#isupper() upper-case letters only
#isspace() identifies whitespaces only
#return bool
print(' \n '.isspace())#True
print(" ".isspace())#True
print("mooo mooo mooo".isspace())#False


#join() ---> string.join(list)
#expects one argument as a list, string is used as a separator
print(",".join(["omicron", "pi", "rho"]))#--->omicron,pi,rho


#lower()
#upper() replaces all upper-case
#makes a copy of a source string, replaces all upper-case letters with their lower-case counterparts
print("SiGmA=60".lower())#---> sigma=60


#lstrip() left strip
#rstrip() right strip
#strip() makes a new string lacking all the leading and trailing whitespaces
#returns a newly created string formed from the original one by removing all leading whitespaces
print("[" + " tau ".lstrip() + "]")#---> [tau ]
#removes all characters enlisted in its argument
print("www.cisco.com".lstrip("w."))#---> cisco.com
print("pythoninstitute.org".lstrip(".org"))#---> pythoninstitute.org


#replace()      #replace(string,string)
#returns a copy of the original string in which all occurrences of the first argument have been replaced by the second argument
print("This is it!".replace("is", "are"))#---> Thare are it!
#replace(string,string,int)
#limit the number of replacements
print("This is it!".replace("is", "are", 1))#---> Thare is it!


#rfind()        #reverse find()
print("tau tau tau".rfind("ta"))#8
print("tau tau tau".rfind("ta", 9))#1
print("tau tau tau".rfind("ta", 3, 9))#-1


#split()        #see join() as reverse method
#splits the string and builds a list of all detected substrings
print("phi       chi\npsi".split())#---> ['phi', 'chi', 'psi']


#swapcase()
#makes a new string by swapping the cases of all letters within the source string
print("I know that I know nothing.".swapcase())#---> i KNOW THAT i KNOW NOTHING.


#title()
#changes every word's first letter to upper-case, turning all other ones to lower-case
print("I know that I know nothing. Part 1.".title())#---> I Know That I Know Nothing. Part 1.