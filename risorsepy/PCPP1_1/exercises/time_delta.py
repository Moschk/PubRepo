'''
- 1 Create a class representing a time interval;
- 2 the class should implement its own method for addition, subtraction on time interval class objects;
- 3 the class should implement its own method for multiplication of time interval class objects by an integer-type value;
- 4 the __init__ method should be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds
        parameters;
- 5 the __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes
        of the time interval object;
- 6 check the argument type, and in case of a mismatch, raise a TypeError exception.

Hint #1
just before doing the math, convert each time interval to a corresponding number of seconds to simplify the algorithm;
for addition and subtraction, you can use one internal method, as subtraction is just ... negative addition.
Test data:
the first time interval (fti) is hours=21, minutes=58, seconds=50
the second time interval (sti) is hours=1, minutes=45, seconds=22
the expected result of addition (fti + sti) is 23:44:12
the expected result of subtraction (fti - sti) is 20:13:28
the expected result of multiplication (fti * 2) is 43:57:40

Hint #2
you can use the assert statement to validate if the output of the __str__ method applied to a time interval object equals the expected value.

PART 2
- 1 Extend the class implementation prepared in the previous lab to support the addition and subtraction of integers to time interval objects;
- 2 to add an integer to a time interval object means to add seconds;
- 3 to subtract an integer from a time interval object means to remove seconds.

Hint
in the case when a special method receives an integer type argument, instead of a time interval object, create a new time interval object based on the integer value.
Test data:
the time interval (tti) is hours=21, minutes=58, seconds=50
the expected result of addition (tti + 62) is 21:59:52
the expected result of subtraction (tti - 62) is 21:57:48
'''

############    soluzione del problema piu' elegante      #############
class TimeInterval:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __add_sub(self, other, operation_type):
        own = self.hours * 3600 + self.minutes * 60 + self.seconds
        another = other.hours * 3600 + other.minutes * 60 + other.seconds

        if operation_type == 'subtraction':
            new_time = own - another
        elif operation_type == 'addition':
            new_time = own + another
        else:
            raise Exception('Unknown operation')

        new_hours = new_time // 3600
        new_minutes = (new_time % 3600) // 60
        new_seconds = new_time % 60

        return TimeInterval(hours=new_hours, minutes=new_minutes, seconds=new_seconds)

    def __add__(self, other):
        if isinstance(other, TimeInterval):
            return self.__add_sub(other, 'addition')
        elif isinstance(other, int):
            return self.__add_sub(TimeInterval(seconds=other), 'addition')
        else:
            raise TypeError('can only add TimeInterval or integer objects')

    def __sub__(self, other):
        if isinstance(other, TimeInterval):
            return self.__add_sub(other, 'subtraction')
        elif isinstance(other, int):
            return self.__add_sub(TimeInterval(seconds=other), 'subtraction')
        else:
            raise TypeError('can only subtract TimeInterval objects')

    def __mul__(self, other):
        if isinstance(other, int):
            new_time = (self.hours * 3600 + self.minutes * 60 + self.seconds) * other
            new_hours = new_time // 3600
            new_minutes = (new_time % 3600) // 60
            new_seconds = new_time % 60
            return TimeInterval(hours=new_hours, minutes=new_minutes, seconds=new_seconds)
        else:
            raise TypeError('can only multiply TimeInterval objects by integers')

    def __str__(self):
        return "%s:%s:%s" % (self.hours, self.minutes, self.seconds)
t1 = TimeInterval(hours=21, minutes=58, seconds=50)
t2 = TimeInterval(1, 45, 22)

assert str(t1 + t2) == '23:44:12'
assert str(t1 - t2) == '20:13:28'
assert str(t1 * 2) == '43:57:40'
assert str(t1 + 62) == '21:59:52'
assert str(t1 - 62) == '21:57:48'

print('It works like a charm')

########## MIA SOLUZIONE #########
class Time_delta:

    def __init__(self, h=0, m=0, s=0):
        self.hours = h
        self.minutes = m
        self.seconds = s
        self.Td_to_secs = h*3600+m*60+s

    def __str__(self):
        return ( str(self.hours) + ':' + str(self.minutes) + ':' + str(self.seconds))

    def __add__(self, delta):
        if isinstance(delta, Time_delta):
            temp = self.Td_to_secs + delta.Td_to_secs
            return secstotd(temp)
        elif isinstance(delta, int):
            t = self.Td_to_secs + delta
            return secstotd(t)
        else: 
            raise TypeError('Moro, solo tra classi Time_delta')
    
    def __sub__(self, delta):
        if isinstance(delta, Time_delta):
            temp = self.Td_to_secs - delta.Td_to_secs
            return secstotd(temp)
        elif isinstance(delta, int):
            t = self.Td_to_secs - delta
            return secstotd(t)
        else: 
            raise TypeError('Moro, solo tra classi Time_delta')
    
    def __mul__(self, mult):
        if isinstance(mult, (int, float)):
            temp = self.Td_to_secs * mult
            h = temp // 3600
            m = (temp - h*3600) // 60
            s = temp % 60
            return Time_delta(h, m, s)
        else: 
            raise TypeError('Moro, solo tra classi Time_delta')

def secstotd(secs):
    new_Td = Time_delta()
    new_Td.hours = secs // 3600
    new_Td.minutes = (secs - new_Td.hours*3600) // 60
    new_Td.seconds = secs % 60
    return new_Td

d0 = 62
d1 = Time_delta(21, 58, 50)

print(d0, d1, sep=' and ')
print(d1+d0, d1-d0, d1*2, sep=' ## ')
print(d0, d1, sep=' and ')
