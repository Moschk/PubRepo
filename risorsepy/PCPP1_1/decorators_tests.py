# DECORATORS FOR TESTING PURPOSES


# DISPLAY TYPES OF ARGUMENTS PASSED
def test_type(my_fun):
    def my_fun_types(*args, **kwargs):
        print('ARGS: ', args)
        for arg in args:
            print(arg, type(arg), sep=' : ', end=' ||\t')
        if len(kwargs) >0:
            print('\nKWARGS: ', kwargs)
            for kwarg in kwargs:
                print(kwarg, type(kwarg), end='\t')
        print()
        return my_fun(*args, **kwargs)
    return my_fun_types

# DISPLAY TIMESTAMP AND TIME
import time
def decorator_timestamp(my_fun): #more general option
    def wrapped_time(*args, **kwargs):
        st = time.gmtime()
        print(time.time(), ' : ', time.strftime("%Y/%m/%d %H:%M:%S"))
        return my_fun(*args, **kwargs)
    return wrapped_time


# simple test
@decorator_timestamp
@test_type
def DDOF(date, date2):
    while len(date) > 1:
        the_sum = 0
        for dig in date:
            the_sum += int(dig)
        date = str(the_sum)
    return date + date2

print(DDOF('123486855', date2='3'))