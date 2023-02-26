#---------------------    -----------------#
'''
 Computers store characters as numbers. There is more than one possible way of encoding characters, but only
 some of them gained worldwide popularity and are commonly used in IT: these are ASCII (used mainly to encode the
 Latin alphabet and some of its derivates) and UNICODE (able to encode virtually all alphabets being used by humans).

2. A number corresponding to a particular character is called a codepoint.

3. UNICODE uses different ways of encoding when it comes to storing the characters using files or computer memory: 
two of them are UCS-4 and UTF-8 (the latter is the most common as it wastes less memory space).
'''

##### STRINGS #####
# treat them as a list, some useful methods follow
'''
1. Python strings are immutable sequences and can be indexed, sliced, and iterated like any other sequence, 
 as well as being subject to the in and not in operators. There are two kinds of strings in Python:

one-line strings, which cannot cross line boundaries – we denote them using either apostrophes ('string') or quotes ("string")
multi-line strings, which occupy more than one line of source code, delimited by trigraphs: ''''''


2. The length of a string is determined by the len() function. The escape character (\) is not counted. For example:

print(len("\n\n"))
 
outputs 2.

3. Strings can be concatenated using the + operator, and replicated using the * operator. For example:

asterisk = '*'
plus = "+"
decoration = (asterisk + plus) * 4 + asterisk
print(decoration)
 
outputs *+*+*+*+*.

4. The pair of functions chr() and ord() can be used to create a character using its codepoint, and to determine a codepoint corresponding to a character. Both of the following expressions are always true:

chr(ord(character)) == character
ord(chr(codepoint)) == codepoint
 


5. Some other functions that can be applied to strings are:

list() – creates a list consisting of all the string's characters;
max() – finds the character with the maximal codepoint;
min() – finds the character with the minimal codepoint.

6. The method named index() finds the index of a given substring inside the string.
'''


### STRING METHODS #####

capitalize() # changes all string letters to capitals;
center() # centers the string inside the field of a known length;
count() # counts the occurrences of a given character;
join() # joins all items of a tuple/list into one string;
lower() # converts all the string's letters into lower-case letters;
lstrip() # removes the white characters from the beginning of the string;
replace() # replaces a given substring with another;
rfind() # finds a substring starting from the end of the string;
rstrip() # removes the trailing white spaces from the end of the string;
split() # splits the string into a substring using a given delimiter;
strip() # removes the leading and trailing white spaces;
swapcase() # swaps the letters' cases (lower to upper and vice versa)
title() # makes the first letter in each word upper-case;
upper() # converts all the string's letter into upper-case letters.

2. String content can be determined using the following methods (all of them return Boolean values):

endswith() # does the string end with a given substring?
isalnum() # does the string consist only of letters and digits?
isalpha() # does the string consist only of letters?
islower() # does the string consists only of lower-case letters?
isspace() # does the string consists only of white spaces?
isupper() # does the string consists only of upper-case letters?
startswith() # does the string begin with a given substring?



##### STRING SORTING AND COMPARISON #####

'''
1. Strings can be compared to other strings using general comparison operators, but comparing them to numbers gives no reasonable
 result, because no string can be equal to any number. For example:

string == number is always False;
string != number is always True;
string >= number always raises an exception.
'''

# Sorting lists of strings can be done by:

sorted() # creating a new, sorted list; 
ex_list = sorted('mario cane')

sort() # which sorts the list in situ
'mario cane'.sort()


# A number can be converted to a string using
str() function.

# A string can be converted to a number (although not every string) using either the 
int() or float() function.
# The conversion fails if a string doesn't contain a valid number image (an exception is raised then).





##### EXCEPTIONS #####

# are classes
# An exception is an event during program execution caused by an abnormal situation. 
# The exception should he handled to avoid the termination of the program. 
# The part of your code that is suspected of being the source of the exception should be put inside the try branch.
# When the exception happens, the execution of the code is not terminated, but instead jumps into the except branch.
# All the predefined Python exceptions form a hierarchy, i.e. some of them are more general (the one named 
# BaseException is the most general one) while others are more or less concrete
# !!!ORDER MATTERS, DON'T PUT LESS CONCRETE ONES BEFORE MORE CONCRETE!!!!

# The code that always runs smoothly.


def reciprocal(n):
    try: # MUST BE PRESENT
    # Risky code.
        n = 1 / n
    except ZeroDivisionError: # optional
    # Crisis management takes place here.
        print("Division failed")
        n = None
    except: # MUST BE PRESENT
    # All other issues fall here.
    else: # optional - branch has to be located after the last except branch
        #executed when (and only when) no exception has been raised inside the try:
        print("Everything went fine")
    finally: # optional
        # always executed, no matter what happened earlier
        # even when raising an exception, no matter whether this has been handled or not
        print("It's time to say goodbye")
        return n

print(reciprocal(2))
print(reciprocal(0))
    
# Back to normal.


##### raise #####
raise ExceptionName
# can raise an exception on demand.
# The same statement, but lacking ExceptionName, can be used inside the try branch only, and raises the same exception 
# which is currently being handled.


##### assert ######
# expression evaluates the expression and raises the AssertError exception when the expression is equal to zero, 
# an empty string, or None. You can use it to protect some critical parts of your code from devastating data.


###### EXCEPTION TREE #######
def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)

print_exception_tree(BaseException)

# args tuple
# property of the Base Exception
# designed to gather all arguments passed to the class constructor
try:
    raise Exception("my", "exception")
except Exception as e: # designed to catch the exception object so you can analyze its nature
    print(e.args)




###### CREATE NEW EXCEPTIONS #######
class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no such pizza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza ready!")

for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)
        