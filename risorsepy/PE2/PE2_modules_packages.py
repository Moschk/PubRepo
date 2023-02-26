#-----------------------MODULES AND PACKAGES-------------------#


###### MODULES #####
# When Python imports a module for the first time
# it translates its contents into a somewhat compiled shape
# The file doesn't contain machine code – it's internal Python semi-compiled code


# import a module, namespaces of names separated (look print)
import os, sys
print(sys.path)

# import 2 functions and 1 constant from a module, their names enter the current namespace
from math import sin, cos, pi
print(sin(pi/2))

# import from a module, use that module with an alias
from math import pi as PI, sin as sine
print(sine(PI/2))

# import all entieties from module, they enter current namespace
from pygame import * ### NOT SAFE ###

# dir() function returns an alphabetically sorted list containing all entities' names available in the module identified by a name
import math
print(dir(math))



##### PSEUDORANDOM MODULES ######
from random import random, seed, randrange, randint, choice, sample

seed() # sets the seed with the current time;
seed(int_value) # sets the seed with the integer value int_value.
randrange(beg = 0, end, step = 0)
randint(left, right) #right-sided exclusion
choice(sequence) # chooses a "random" element from the input sequence and returns it
sample(sequence, elements_to_choose) # builds a list (a sample) consisting of the elements_to_choose element "drawn" from the input sequence



##### PLATFORM MODULE #####
#platform module lets you access the underlying platform's data, i.e., hardware, operating system, and interpreter version information
from platform import platform, machine, processor, system, version, \
    python_implementation, python_version_tuple
 
print(machine()) # generic name of the processor x86
print(platform()) # operating system Windows 11 ver
print(processor()) # processor name AMD Athlon x4
print(system()) # generic OS name Linux
print(version()) # version of OS
print(python_implementation()) # Python implementation CPython
print(python_version_tuple()) # (major, mino, patch) Python version number



##### PACKAGES #####
'''
1. While a module is designed to couple together some related entities such as functions, variables, or constants,
 a package is a container which enables the coupling of several related modules under one common name. 
 Such a container can be distributed as-is (as a batch of files deployed in a directory sub-tree) or 
 it can be packed inside a zip file.

2. During the very first import of the actual module, Python translates its source code into a semi-compiled format 
stored inside the pyc files, and deploys these files into the __pycache__ directory located in the module's home directory.


3. If you want to tell your module's user that a particular entity should be treated as private (i.e. not to be explicitly 
used outside the module) you can mark its name with either the _ or __ prefix. Don't forget that this is only a recommendation, 
not an order.


4. The names shabang, shebang, hasbang, poundbang, and hashpling describe the digraph written as #!, used to instruct 
Unix-like OSs how the Python source file should be launched. This convention has no effect under MS Windows.


5. If you want convince Python that it should take into account a non-standard package's directory, its name needs to be 
inserted/appended into/to the import directory list stored in the path variable contained in the sys module.


6. A Python file named __init__.py is implicitly run when a package containing it is subject to import, and is used to 
initialize a package and/or its sub-packages (if any). The file may be empty, but must not be absent.
'''
#!/usr/bin/env python3
from sys import path
 
path.append('..∖∖packages') # location of the tree of folders with modules
 
import extra.good.best.sigma as sig # extra.good.best are folders, sigma a module
import extra.good.alpha as alp
 
print(sig.funS())
print(alp.funA())
 
# can also be a zip file
#!/usr/bin/env python3
from sys import path
 
path.append('..∖∖packages∖∖extrapack.zip')
 
import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import funI
from extra.good.beta import funB # extra.good are folders, beta a module and funB a function
 
print(sig.funS())
print(alp.funA())
print(funI())
print(funB())


##### PIP #####
'''
1. A repository (or repo for short) designed to collect and share free Python code exists and works under the name
 Python Package Index (PyPI) although it's also likely that you come across the very niche name The Cheese Shop. 
 The Shop's website is available at https://pypi.org/.

2. To make use of The Cheese Shop, a specialized tool has been created and its name is pip (pip installs packages while 
pip stands for... ok, never mind). As pip may not be deployed as a part of the standard Python installation, 
it is possible that you will need to install it manually. Pip is a console tool.

3. To check pip's version one the following commands should be issued:
pip --version 
or
pip3 --version

4. The list of the main pip activities looks as follows:

pip help operation – shows a brief description of pip;
pip list – shows a list of the currently installed packages;
pip show package_name – shows package_name info including the package's dependencies;
pip search anystring – searches through PyPI directories in order to find packages whose names contain anystring;
pip install name – installs name system-wide (expect problems when you don't have administrative rights);
pip install --user name – installs name for you only; no other platform user will be able to use it;
pip install -U name – updates a previously installed package;
pip uninstall name – uninstalls a previously installed package.
'''