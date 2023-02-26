'''Create a function decorator that prints a timestamp 
(in a form like year-month-day hour:minute:seconds, eg. 2019-11-05 08:33:22)
Create a few ordinary functions that do some simple tasks, like adding or multiplying two numbers.
Apply your decorator to those functions to ensure that the time of the function executions can be monitored.'''

import time

def decorator_timestamp(my_fun): #more general option
    def wrapped_time(*args, **kwargs):
        st = time.gmtime()
        print(time.strftime("%Y/%m/%d %H:%M:%S",st))
        return my_fun(*args, **kwargs)
    return wrapped_time

def decorator_timestamp(my_fun): # more specific
    def wrapped_time(t, y):
        st = time.gmtime()
        print(time.strftime("%Y/%m/%d %H:%M:%S",st))
        return my_fun(t, y)
    return wrapped_time

@decorator_timestamp
def addiction(a, b):
    return a+b

@decorator_timestamp
def multi(a, b):
    return a*b

print('la somma di 3 e 5 e\': ', addiction(3, 5))

time.sleep(2)

print('la moltiplicazione invece: ', multi(3, 5))





'''Scenario 2 
1 Create a class representing a luxury watch;
    The class should allow you to hold a number of watches created in the watches_created class variable. 
    The number could be fetched using a class method named get_number_of_watches_created;
2 the class may allow you to create a watch with a dedicated engraving (text). 
    As this is an extra option, the watch with the engraving should be created using an alternative constructor (a class method), as a regular __init__ method should not allow ordering engravings
3 the regular __init__ method should only increase the value of the appropriate class variable;
4 The text intended to be engraved should follow some restrictions:

it should not be longer than 40 characters;
it should consist of alphanumerical characters, so no space characters are allowed;
if the text does not comply with restrictions, an exception should be raised;
before engraving the desired text, the text should be validated against restrictions using a dedicated static method.

Create a watch with no engraving
Create a watch with correct text for engraving
Try to create a watch with incorrect text, like 'foo@baz.com'. Handle the exception
After each watch is created, call class method to see if the counter variable was increased'''



class LuxuryWatch:
    watches_created = 0

    def __init__(self):
        LuxuryWatch.watches_created += 1

    @classmethod
    def get_number_of_watches_created(cls):
        return cls.watches_created

    @classmethod
    def with_engraving(cls, text):
        if LuxuryWatch.check_text(text):
            _watch = cls()
            _watch.text = text
            return _watch
        else:
            raise Exception(text + ' - it does not follow the "alpha" rule')

    @staticmethod
    def check_text(text):
        if len(text) > 40:
            return False
        if not text.isalpha():
            return False
        return True

# my solution
class Luxury_watch:
    watched_created = 0

    def __init__(self):
        self.engraved = ''
        Luxury_watch.watched_created += 1

    @classmethod
    def engrave_watch(cls, text):
        try:
            if (text.isalnum() and len(text)<41 and ' ' not in text):
                _eng_watch = cls()
                _eng_watch.engraved = text
                return _eng_watch
            else: raise
        except:
            print("Only alphanumeric char with no spaces allowed, thx")
    

plain_watch =  Luxury_watch()
print(Luxury_watch.watched_created)
valid_watch = Luxury_watch.engrave_watch('amamiiiii')
print(Luxury_watch.watched_created)
invalid_watch = Luxury_watch.engrave_watch('&&&87565ff /')
print(Luxury_watch.watched_created)