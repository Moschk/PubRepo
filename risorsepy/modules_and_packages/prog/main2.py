'''
MUST BE PRESENT ANYWHERE IN THE PACKAGE THE FILE __init__ (EVEN IF EMPTY)
'''
from sys import path
from pprint import pprint

pprint(path)
print('-'*30)
path.append('risorsepy\modules_and_packages\packages')
#path.append('c:\\Users\\dermo\\Documents\\Python\\risorsepy\\modules_and_packages\\packages')
pprint(path)

#import from package method 1
import extra.iota
print(extra.iota.FunI())
#method 2
from extra.iota import FunI
print(FunI())

import extra.good.best.sigma
from extra.good.best.tau import FunT
 
print(extra.good.best.sigma.FunS())
print(FunT())

#ALIASING
import extra.good.best.sigma as sig
import extra.good.alpha as alp
 
print(sig.FunS())
print(alp.FunA())

#SEE main_zip FOR ZIP PACKAGE IMPORT