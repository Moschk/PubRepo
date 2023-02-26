###### GENERATORS ######

# piece of specialized code able to produce a series of values, and to control the iteration process
# very similar to an ITERATOR

# range() function


# The ITERATOR PROTOCOL is a way in which an object should behave to conform to the rules imposed 
# by the context of the for and in statements.
# ITERATOR An object conforming to the iterator protocol is 
# An iterator must provide two methods:
#    __iter__() which should return the object itself and which is invoked once
#       (it's needed for Python to successfully start the iteration)
#    __next__() which is intended to return the next value (first, second, and so on) of the desired series
#        – it will be invoked by the for/in statements in order to pass through the next iteration; if there are no more values to provide,
#          the method should raise the StopIteration exception.

class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")		
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

for i in Fib(10):
    print(i)



# yield keyword
# just like return, but doesn't lose the state of the function
def fun(n):
      for i in range(n):
         yield i
# such a function should not be invoked explicitly as – in fact – it isn't a function anymore; it's a generator object
# The invocation will return the object's identifier, not the series we expect from the generator.

# Generators may also be used within list comprehensions
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
t = [x for x in powers_of_2(5)]
print(t)

# list() function can transform a series of subsequent generator invocations into a real list
t = list(powers_of_2(3))
print(t)

# the context created by the in operator allows you to use a generator
for i in range(20):
    if i in powers_of_2(4):
        print(i)



# LIST COMPREHENSION and generators
list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)
#equals to
list_2 = [10 ** ex for ex in range(6)]


the_list = []
for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)
#equals to
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]


# LIST COMPREHENSION ARE NOT GENERATORS
the_list = [1 if x % 2 == 0 else 0 for x in range(10)] # LIST, the list is created (and iterated through) as a whole
the_generator = (1 if x % 2 == 0 else 0 for x in range(10)) # GENERATOR parentheses, exists when the loop is being executed.
 
for v in the_list:
    print(v, end=" ")
print()
 
for v in the_generator:
    print(v, end=" ")
print()
#this generator has NO LENGHT




###### LAMBDA ######
# anonymous function created on the go
# lambda parameters: expression
# returns the value of the expression when taking into account the current value of the current lambda argument

pwr = lambda x, y: x ** y
pwr(2, 4) # return 16 


# map() function
# map(function, iterable)
# function applies the function passed by its first argument to all its second argument's elements,
#   and returns an iterator delivering all subsequent function results
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()


# filter()
# filters its second argument while being guided by directions flowing from the function specified as the first argument
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)


##### CLOSURES #####
# closure is a technique which allows the storing of values in spite of the fact that the context 
#   in which they have been created does not exist anymore
def outer(par):
    loc = par
    def inner():
        return loc
    return inner

var = 1
fun = outer(var) # outer() invocation is a closure
print(fun())

#  It is fully possible to declare a closure equipped with an arbitrary number of parameters
def make_closure(par):
    loc = par
    def power(p):
        return p ** loc
    return power

fsqr = make_closure(2)
fcub = make_closure(3)
for i in range(5):
    print(i, fsqr(i), fcub(i))




#--------------------FILES--------------------------#

# ACCESS
# Windows file names must be written as follows:
name = "\\dir\\file"
#  will work for Windows, Python can convert it, used for Unix /
name = "c:/dir/file"



# FILE STREAMS
# The opening of the stream is not only associated with the file, but should also declare the manner in which the stream will be processed.
#   This declaration is called an open mode.
# If the opening is successful, the program will be allowed to perform only the operations which are consistent with the declared open mode

# There are two basic operations performed on the stream:
# 1. read from the stream: the portions of the data are retrieved from the file and placed in a memory area managed by the program (e.g., a variable);
# 2. write to the stream: the portions of the data from the memory (e.g., a variable) are transferred to the file.

# There are three basic modes used to open the stream:
# A. read mode: a stream opened in this mode allows read operations only; trying to write to the stream will cause an exception (the exception is named UnsupportedOperation, which inherits OSError and ValueError, and comes from the io module);
# B. write mode: a stream opened in this mode allows write operations only; attempting to read the stream will cause the exception mentioned above;
# C. update mode: a stream opened in this mode allows both writes and reads.

# Whenever we talk about reading from and writing to the stream, try to imagine this analogy.
# The programming books refer to this mechanism as the current file position



# FILE HANDLING
# The operations you're allowed to use are imposed by the way in which you've opened the file

# Note: you never use constructors to bring these objects to life. The only way you obtain them is to invoke the function named open().
# The function analyses the arguments you've provided, and automatically creates the required object.
# If you want to get rid of the object, you invoke the method named close().

# Due to the type of the stream's contents, all the streams are divided into text and binary streams.
#   1. The text streams are structured in lines; that is, they contain typographical characters (letters, digits, punctuation, etc.) 
#    arranged in rows (lines), as seen with the naked eye when you look at the contents of the file in the editor.

#   2. The binary streams don't contain text but a sequence of bytes of any value. This sequence can be, for example, an executable program,
#    an image, an audio or a video clip, a database file, etc.

# During reading/writing of lines from/to the associated file, nothing special occurs in the Unix environment, but when the same operations are
#  performed in the Windows environment, a process called a translation of newline characters occurs: when you read a line from the file, 
#  every pair of \r\n characters is replaced with a single \n character, and vice versa; during write operations, every \n character is replaced 
#  with a pair of \r\n characters; the mechanism is completely transparent

# OPENING
stream = open(file_path_as_string, mode = 'r', encoding = None)

# r open mode: read
#   the stream will be opened in read mode;
#   the file associated with the stream must exist and has to be readable, otherwise the open() function raises an exception.

# w open mode: write
#   the stream will be opened in write mode;
#   the file associated with the stream doesn't need to exist; if it doesn't exist it will be created; if it exists, 
#   it will be truncated to the length of zero (erased); if the creation isn't possible (e.g., due to system permissions) 
#   the open() function raises an exception.

# a open mode: append
#   the stream will be opened in append mode;
#   the file associated with the stream doesn't need to exist; if it doesn't exist, it will be created;
#   if it exists the virtual recording head will be set at the end of the file (the previous content of the file remains untouched.)

# r+ open mode: read and update
#   the stream will be opened in read and update mode;
#   the file associated with the stream must exist and has to be writeable, otherwise the open() function raises an exception;
#   both read and write operations are allowed for the stream.

# w+ open mode: write and update
#   the stream will be opened in write and update mode;
#    the file associated with the stream doesn't need to exist; if it doesn't exist, it will be created; the previous content of the file remains untouched;
#    both read and write operations are allowed for the stream.

# Selecting text and binary modes
# If there is a letter b at the end of the mode string, it means that the stream is to be opened in binary mode.
# If the mode string ends with a letter t, the stream is opened in text mode.
# Text mode is the default behaviour assumed when no binary/text mode specifier is used.

# Finally, the successful opening of a file will set the current file position (the virtual reading/writing head) 
# before the first byte of the file if the mode is not a and after the last byte of the file if the mode is set to a.

# Text mode	Binary mode	Description
# rt	rb	read
# wt	wb	write
# at	ab	append
# r+t	r+b	read and update
# w+t	w+b	write and update

#   EXTRA  
# You can also open a file for its exclusive creation. You can do this using the x open mode.
# If the file already exists, the open() function will raise an exception.

try:
    stream = open("C:\Users\User\DesktopFile.txt", "rt")
    # Processing goes here.
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)
 

# PRE OPENED STREAMS

# sys.stdin (as standard input)
# the stdin stream is normally associated with the keyboard, pre-open for reading and regarded as the primary data source for the running programs;
# the well-known input() function reads data from stdin by default.

# sys.stdout (as standard output)
# the stdout stream is normally associated with the screen, pre-open for writing, regarded as the primary target for outputting data by the running program;
# the well-known print() function outputs the data to the stdout stream.

# sys.stderr (as standard error output)
# the stderr stream is normally associated with the screen, pre-open for writing, regarded as the primary place where the running program 
#   should send information on the errors encountered during its work;

# the separation of stdout (useful results produced by the program) from the stderr (error messages, undeniably useful but does not provide results)
# gives the possibility of redirecting these two types of information to the different targets. More extensive discussion of this issue is beyond
# the scope of our course. The operation system handbook will provide more information on these issues.



# CLOSING STREAMS
# The last operation performed on a stream (this doesn't include the stdin, stdout, and stderr streams, which don't require it) should be closing.

# That action is performed by a method invoked from within the open stream object
# stream.close().

# the name of the function is definitely self-commenting: close()
# the function expects exactly no arguments; the stream doesn't need to be opened
# the function returns nothing, but raises an IOError exception in case of error;
# most developers believe that the close() function always succeeds and thus there is no need to check if it's done its task properly.

# Since the closing of the stream forces the buffers to flush them, it may be that the flushes fail and therefore the close() fails too.



# DIAGNOSING STREAM PROBLEM
# IOError is equipped with the useful proprerty errno

try:
    # Some stream operations.
except IOError as exc:
    print(exc.errno)
# errno.EACCES → Permission denied
# errno.EEXIST → File exists
# errno.EFBIG → File too large
# errno.EISDIR → Is a directory
# errno.EMFILE → Too many open files
# errno.ENOENT → No such file or directory
# errno.ENOSPC → No space left on device

import errno
try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)
        

# strerror() simplify the error handling code
from os import strerror
try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))



#--------------PROCESSING TEXT FILES---------------------#

# # read() method
# If applied to a text file's stream, the function is able to:
#   - read a desired number of characters (including just one) from the stream, and return them as a string;
#   - read all the stream contents, and return them as a string;
#   - if there is nothing more to read (the virtual reading head reaches the end of the file's stream), the function returns an empty string.
from os import strerror
try:
    counter = 0
    stream = open('text.txt', "rt")
    char = stream.read(1) # reads one char at a time
    while char != '':
        print(char, end='')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\n\nCharacters in file:", counter)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
#!!!!! Remember – reading a terabyte-long file using this method may corrupt your OS !!!!!!!#

counter = 0
stream = open('text.txt', "rt")
content = stream.read()# reads all the content
for char in content:
    print(char, end='')
    counter += 1
stream.close()
print("\n\nCharacters in file:", counter)


# readline() method
# read a complete line of text from the file, and returns it as a string in the case of success
from os import strerror
try:
    character_counter = line_counter = 0
    stream = open('text.txt', 'rt')
    line = stream.readline()
    while line != '':
        line_counter += 1
        for char in line:
            print(char, end='')
            character_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nCharacters in file:", character_counter)
    print("Lines in file:     ", line_counter)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# readlines()
# tries to read all the file contents, and returns a list of strings, one element per file line
# If you're not sure if the file size is small enough and don't want to test the OS, you can convince it 
# to read not more than a specified number of bytes at once (the returning value remains the same – it's a list of a string).
from os import strerror
try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20) # The maximum accepted input buffer size is passed to the method as its argument.
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
# You may expect that readlines() can process a file's contents more effectively than readline(), as it may need to be invoked fewer times.
# Note: when there is nothing to read from the file, the method returns an empty list. Use it to detect the end of the file.
# There are two nested loops in the code: the outer one uses readlines()'s result to iterate through it, while the inner one prints the lines character by character.
# the object is an instance of the iterable class.
# The iteration protocol defined for the file object is very simple – its __next__ method just returns the next line read in from the file.
# the object automatically invokes close()


# write()
# it expects just one argument 
# writing a file opened in read mode won't succeed
from os import strerror
try:
	file = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for char in s:
			file.write(char)
	file.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))
    
# Note: you can use the same method to write to the stderr stream, but don't try to open it, as it's always open implicitly.
# For example, if you want to send a message string to stderr to distinguish it from normal program output, it may look like this:

import sys
sys.stderr.write("Error message")





#-------------------------------BYTEARRAY------------------------#
# Amorphous data is data which have no specific shape or form
# specialized class name bytearray – as the name suggests, it's an array containing (amorphous) bytes

data = bytearray(10)
# Such an invocation creates a bytearray object able to store ten bytes.
# Note: such a constructor fills the whole array with zeros.

# mutable
# subject of the len()
# can access any of their elements using conventional indexing
# treat any byte array elements as integer values
# you mustn't set any byte array elements with a value which is not an integer (TypeError exception)
# not allowed to assign a value that doesn't come from the range 0 to 255 inclusive (ValueError exception)

# WRITE A BYTEARRAY
from os import strerror
data = bytearray(10)
for i in range(len(data)):
    data[i] = 10 + i
try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
# The write() method returns a number of successfully written bytes.


# readinto()
# Reading from a binary file requires the use of a specialized method name readinto(), as the method doesn't create a new byte array object,
#  but fills a previously created one with the values taken from the binary file.
# Note:
#   the method returns the number of successfully read bytes;
#   the method tries to fill the whole space available inside its argument; if there are more data in the file than space in the argument,
#   the read operation will stop before the end of the file; otherwise, the method's result may indicate that the byte array has only been filled
#   fragmentarily (the result will show you that, too, and the part of the array not being used by the newly read contents remains untouched)

from os import strerror
data = bytearray(10)
try:
    binary_file = open('file.bin', 'rb')
    binary_file.readinto(data)
    binary_file.close()
    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
    

# read()
# read all the contents of the file into the memory, making them a part of object of the bytes class
# BUT IT'S IMMUTABLE
# CAN FILL ALL THE MEMORY
from os import strerror
try:
    binary_file = open('file.bin', 'rb')
    data = bytearray(binary_file.read())
    binary_file.close()
    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# if read() method is invoked with an argument, it specifies the maximum number of bytes to be read




################ Evaluating students' results ##############
# A base exception class for our code:
class StudentsDataException(Exception):
    pass

# An exception for erroneous lines:
class WrongLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__(self)
        self.line_number = line_number
        self.line_string = line_string

# An exception for an empty file.
class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__(self)

from os import strerror

# A dictionary for students' data:
data = { }

file_name = input("Enter student's data filename: ")
line_number = 1
try:
    f = open(file_name, "rt")
    # Read the whole file into list.
    lines = f.readlines()
    f.close()
    # Is the file empty?
    if len(lines) == 0:
        raise FileEmpty()
    # Scan the file line by line.
    for i in range(len(lines)):
        # Get the i'th line.
        line = lines[i]
        # Divide it into columns.
        columns = line.split()
        # There shoule be 3 columns - are they there?
        if len(columns) != 3:
            raise WrongLine(i + 1, line)
        # Build a key from student's given name and surname.
        student = columns[0] + ' ' + columns[1]
        # Get points.
        try:
            points = float(columns[2])
        except ValueError:
            raise WrongLine(i + 1, line)
        # Update dictionary.
        try:
            data[student] += points
        except KeyError:
            data[student] = points
    # Print results.
    for student in sorted(data.keys()):
        print(student,'\t', data[student])

except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
except WrongLine as e:
    print("Wrong line #" + str(e.line_number) + " in source file:" + e.line_string)
except FileEmpty:
    print("Source file empty")


'''
The following statement:

assert var != 0

will stop the program when var == 0
'''