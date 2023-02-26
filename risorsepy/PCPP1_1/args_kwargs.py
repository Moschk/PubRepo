#----------------- ARGS, KWARGS -------------------------#
'''
These two special identifiers (named *args and **kwargs) should be put as the last two parameters in a function definition.
Their names could be changed because it is just a convention to name them 'args' and 'kwargs', but it’s more important to sustain the order of the parameters and leading asterisks.

Those two special parameters are responsible for handling any number of additional arguments (placed next after the expected arguments) passed to a called function:

*args – refers to a tuple of all additional, not explicitly expected positional arguments, so arguments passed without keywords and passed next after the expected arguments.
    In other words, *args collects all unmatched positional arguments;
**kwargs (keyword arguments) – refers to a dictionary of all unexpected arguments that were passed in the form of keyword=value pairs.
    Likewise, **kwargs collects all unmatched keyword arguments.
In Python, asterisks are used to denote that args and kwargs parameters are not ordinary parameters and should be unpacked, as they carry multiple items.

If you’ve ever programmed in the C or C++ languages, then you should remember that the asterisk character has another meaning (it denotes a pointer) which could be misleading for you.
'''
def combiner(a, b, *args, **kwargs):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))
    print(kwargs, type(kwargs))


combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')


# Python offers complex parameter handling:

# positional arguments (a,b) are distinguished from all other positional arguments (args)
# the keyword 'c' is distinguished from all other keyworded parameters

def combiner(a, b, *args, c=20, **kwargs):
    super_combiner(c, *args, **kwargs)
def super_combiner(my_c, *my_args, **my_kwargs):
    print('my_args:', my_args)      # (1, 1)
    print('my_c:', my_c)            # 2
    print('my_kwargs', my_kwargs)   # {'argument1': 1, 'argument2': '1'}
combiner(1, '1', 1, 1, c=2, argument1=1, argument2='1')

#in recursive function, you can pass args and kwargs as the argument of the rec_fun
#ONLY WITH *args **kwargs (* needed to unpack tuple for the call)
#when you use them in the body args is already unpacked by the function call fun(*args)
def simmetric_diff(*args):
    set_diff = []
            
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

    else: 
        args = args[1:]
        return simmetric_diff(args[0], simmetric_diff(*args))

set1 = [1,2,2,3]
set2 = [1,3,4,4]
set3 = [4,5,5,7]

print(simmetric_diff(set1, set2, set3))


#----------------DECORATORS-------------------#

