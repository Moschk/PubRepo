# Prof. Jekyll conducts classes with students and regularly makes notes in a text file.
# Each line of the file contains three elements: the student's first name, the student's last name,
# and the number of points the student received during certain classes.

# The elements are separated with white spaces. Each student may appear more than once inside
# Prof. Jekyll's file.

# Your task is to write a program which:

# asks the user for Prof. Jekyll's file name;
# reads the file contents and counts the sum of the received points for each student;
# prints a simple (but sorted) report, just like this one:
# Andrew   Cox      1.5
# Anna     Boleyn   15.5
# John     Smith    7.0
# Output

# Note:

# your program must be fully protected against all possible failures:
#   the file's non-existence,
#   the file's emptiness,
#   or any input data failures;
# encountering any data error should cause
# immediate program termination, and the error should be presented to the user;
# implement and use your own exceptions hierarchy – we've presented it in the editor;
# the second exception should be raised when a wrong line is detected,
# and the third when the source file exists but is empty.
# Tip: Use a dictionary to store the students' data.

class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):#should be raised when a wrong line is detected
    def __init__(self, linea):
        super().__init__(self)
        self.lalinea = linea

class FileEmpty(StudentsDataException):#when the source file exists but is empty
    def __init__(self):
        super().__init__(self)

# asks the user for Prof. Jekyll's file name;
try:
    file_name = input('Name file: ')
    file = open(file_name, 'rt')
    print('Apertoooo!')
    lines = file.readlines()
    file.close()
    print('Chiusoooo!')
    print(lines)
    if len(lines) == 0: raise FileEmpty

    try:# reads the file contents and counts the sum of the received points for each student;
        dict_reg = {}
        for line in lines: #prendi i caratteri e forma la chiave, poi prendi il numero e aggionra il valore

            #######

    except:
        print('siamo fottuti')
    # prints a simple (but sorted) report

except FileEmpty:
    print('empty')
except FileNotFoundError as err:
    print(err)
except BaseException as baseexc:
    print('last hope', baseexc)