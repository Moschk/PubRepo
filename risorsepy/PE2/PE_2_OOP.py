#------------OBJECT ORIENTED PROGRAMMING-------------#

# CLASS
# You can perform two important activities specific to many objective languages
# INTROSPECTION, which is the ability of a program to examine the type or properties of an object at runtime;
# REFLECTION, which goes a step further, and is the ability of a program to manipulate the values, properties
#   and/or functions of an object at runtime.
class TheSimplestClass:
    pass

class_object = TheSimplestClass() # class instance

#SUBCLASS
class Subclass(TheSimplestClass):
    pass

subclass_object = Subclass() # subclass instance



# STACK 

class Stack:
    ### CONSTRUCTOR __init__
    # function, as its general purpose is to construct a new object (hidden to the user)
    # has to have at least one parameter - self
    # the parameter is used to represent the newly created object
    # you can use the parameter to manipulate the object
    # cannot return a value, as it is designed to return a newly created object and nothing else
    # cannot be invoked directly either from the object or from inside the class
    def __init__(self):
        self.__stack_list = [] # hidden cause __ double underscore

    # function (method) of the class
    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

''' NOTA BENE
- different objects of the same class may possess different sets of properties;
- there must be a way to safely check if a specific object owns the property you want to utilize (unless you want to provoke an exception – it's always worth considering)
- each object carries its own set of properties – they don't interfere with one another in any way.'
- modifying an instance variable of any object has no impact on all the remaining objects
'''
class ExampleClass:
    def __init__(self, val = 1):
        self.first = val # instance variable created when the object instance is created
 
    def set_second(self, val):
        self.second = val # instance variable created when the class method is called



# PREDEFINED PROPRIETIES AND METHODS

# __dict__ variable (dictionary)
# contains the names and values of all the properties (variables) the object is currently carrying
example_object_2 = ExampleClass(2)
example_object_2.set_second(3)
print(example_object_2.__dict__) # OUTPUT: {'second': 3, 'first': 2}
print(ExampleClass.__dict__)

# __name__ variable
# string, contains the name of the class
# exists only inside classes
print(ExampleClass.__name__)

# __module__ variable
# stores the name of the module which contains the definition of the class
print(ExampleClass.__module__) # OUTPUT __main__ -> file being run
print(obj.__module__)

# __bases__ tuple
# contains classes (not class names) which are direct superclasses for the class.
# The order is the same as that used inside the class definition.
# only classes have this attribute
print(Subclass.__bases__)
#Note: a class without explicit superclasses points to an object (a predefined Python class) as its direct ancestor.

# __str__() function
# the way in which the object is able to introduce itself by default <__main__.Star object at 0x7f1074cc7c50>
# You can change it just by defining your own method of the name
class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy
    def __str__(self):
        return self.name + ' in ' + self.galaxy
sun = Star("Sun", "Milky Way")
print(sun)
#OUTPUT Sun in Milky Way




# MANGLING
class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val

example_object_2 = ExampleClass(2)
example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.__third = 5

print(example_object_2.__dict__) # {'_ExampleClass__first': 2, '_ExampleClass__second': 3}
print(example_object_3.__dict__) # {'_ExampleClass__first': 4, '__third': 5}

# As you can see, making a property private is limited.
# The mangling won't work if you add a private instance variable outside the class code.
# In this case, it'll behave like any other ordinary property.



# CLASS VARIABLES
# exists in exactly one copy
# aren't shown in an object's __dict__
# always presents the same value in all class instances (objects)
class ExampleClass:
    counter = 0 # class variable
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1

example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_2.__dict__, example_object_2.counter) # {'_ExampleClass__first': 2} 2
print(example_object_3.__dict__, example_object_3.counter) # {'_ExampleClass__first': 4} 2




# hasattr() function
# find out if a class variable is available
# returns True if the specified class contains a given attribute, and False otherwise
hasattr(ExampleClass, 'prop')
hasattr(ExampleClass, 'b')

# type() function
# find the class of a particular object
print(type(obj))
print(type(obj).__name__) # find the name of the object's class




##### METHODS #####
# function embedded inside a class.

# is obliged to have at least one parameter
# may be invoked without an argument, but not declared without parameters
# The first (or only) parameter is usually named self (convention)
# used to obtain access to the object's instance and class variables
class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)

    def __hidden(self):
        print("hidden")
 
obj = Classy()
obj.var = 3
obj.method()
obj._Classy__hidden() # NOT  obj.__hidden -> PRIVATE THEN MANGLING



##### INHERITANCE #####
# -Methods as well as instance and class variables defined in a superclass are automatically
#   inherited by their subclasses
# -In order to find any object/class property, Python looks for it inside:
#   1. the object itself;
#   2. all classes involved in the object's inheritance line from bottom to top;
#   3. if there is more than one class on a particular inheritance path, Python scans them from left to right;
#   4. if both of the above fail, the AttributeError exception is raised.
# -If any of the subclasses defines a method/class variable/instance variable of the same name as existing in the superclass,
#   the new name overrides any of the previous instances of the name

# issubclass()
# check if a particular class is a subclass of any other class
# NB a class is a subclass of its own
issubclass(ClassOne, ClassTwo)
# returns True if ClassOne is a subclass of ClassTwo, and False otherwise

# isinstance()
# checks if an object comes from an indicated class
isinstance(mickey, Mouse)

# is keyword
# checks if two variables refer to the same object (puntano come indirizzo memoria)
class Mouse:
    pass
 
mickey = Mouse()
minnie = Mouse()
cloned_mickey = mickey
print(mickey is minnie, mickey is cloned_mickey)

# super() function
# parameterless
# returns a reference to the nearest superclass of the class
class Mouse:
    def __str__(self):
        return "Mouse"
 
 
class LabMouse(Mouse):
    def __str__(self):
        return "Laboratory " + super().__str__()
 
 
doctor_mouse = LabMouse();
print(doctor_mouse) # Prints "Laboratory Mouse".


