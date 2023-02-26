'''
You are about to create a multifunction device (MFD) that can scan and print documents;
the system consists of a scanner and a printer;
your task is to create blueprints for it and deliver the implementations;

1.create an abstract class representing a scanner that enforces the following methods:
    1.scan_document – returns a string indicating that the document has been scanned;
    2.get_scanner_status – returns information about the scanner (max. resolution, serial number)

2.Create an abstract class representing a printer that enforces the following methods:
    1.print_document – returns a string indicating that the document has been printed;
    2.get_printer_status – returns information about the printer (max. resolution, serial number)

import abc
class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass

'''
import abc

class Scanner(abc.ABC):
    def scan_document():
        return print('Scan mission complete!')
    
    @abc.abstractmethod
    def get_scanner_status():#returns information about the scanner (max. resolution, serial number)
        pass

class Printer(abc.ABC):
    def print_document():
        return print('Print mission complete!')
    
    @abc.abstractmethod
    def get_printer_status():#returns information about the printer (max. resolution, serial number)
        pass
'''
3.Create MFD1, MFD2 and MFD3 classes that inherit the abstract classes responsible for scanning and printing:
    1.MFD1 – should be a cheap device, made of a cheap printer and a cheap scanner, so device capabilities 
        (resolution) should be low;
    2.MFD2 – should be a medium-priced device allowing additional operations like printing operation history, 
        and the resolution is better than the lower-priced device;
    3.MFD3 – should be a premium device allowing additional operations like printing operation history and fax machine.

Instantiate MFD1, MFD2 and MFD3 to demonstrate their abilities.
All devices should be capable of serving generic feature sets.
'''
class MFD1(Scanner, Printer):
    def __init__(self, serial_n):
        self.res = '640x480'
        self.s_num = serial_n
    
    def get_printer_status(self):
        return print(self.res, self.s_num)
    
    def get_scanner_status(self):
        return print(self.res, self.s_num)
        
class MFD2(Scanner, Printer):
    def __init__(self, serial_n):
        self.res = '1366x720'
        self.s_num = serial_n
        self.history = []

    def get_printer_status(self):
        return print(self.res, self.s_num)
    
    def get_scanner_status(self):
        return print(self.res, self.s_num)

    def print_history(self):
        return self.history
    
class MFD3(Scanner, Printer):
    def __init__(self, serial_n):
        self.res = '1366x720'
        self.s_num = serial_n
        self.history = []

    def get_printer_status(self):
        return print(self.res, self.s_num)
    
    def get_scanner_status(self):
        return print(self.res, self.s_num)

    def print_history(self):
        return self.history
    
    def fax():
        pass

povery = MFD1(115)
borghesi = MFD2(226)
rikki = MFD3(3356)

borghesi.get_scanner_status()