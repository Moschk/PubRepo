#ZIP PACKAGE IMPORT
from sys import path
path.append('risorsepy\modules_and_packages\packages\extrapack.zip')
 
import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import FunI
from extra.good.beta import FunB
 
print(sig.FunS())
print(alp.FunA())
print(FunI())
print(FunB())