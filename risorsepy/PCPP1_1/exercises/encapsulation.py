'''
1.Implement a class representing an account exception,
2.Implement a class representing a single bank account,
    1.This class should control access to the account number and account balance 
        attributes by implementing the properties:
        2.it should be possible to read the account number only, not change it. 
            In case someone tries to change the account number, raise an alarm by raising an exception;
        3.it should not be possible to set a negative balance. 
            In case someone tries to set a negative balance, raise an alarm by raising an exception;
        4.when the bank operation (deposit or withdrawal) is above 100.000, then
            additional message should be printed on the standard output (screen) for auditing purposes;
        5.it should not be possible to delete an account as long as the balance is not zero;

test your class behavior by:
setting the balance to 1000;
trying to set the balance to -200;
trying to set a new value for the account number;
trying to deposit 1.000.000;
trying to delete the account attribute containing a non-zero balance.
'''

class AccountException(Exception):
    pass

class Account:
    def __init__(self, number):
        self.__balance = 0
        self.__number = number
        pass

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise AccountException('Can not set negative value')

        if abs(self.__balance - value) > 100_000:
            print('This operation will be audited')

        self.__balance = value

    @balance.deleter
    def balance(self):
        if self.__balance > 0:
            raise AccountException('Can not delete account as long it is not empty')
        self.__balance = None

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        raise AccountException('Invalid operation')

    @number.deleter
    def number(self):
        raise AccountException('Invalid operation')

    def __str__(self):
        return 'Account #{} balance is {}'.format(self.__number, self.__balance)

account = Account('34-6514-7654-9999-0002')
account.balance += 1000
print(account)

try:
    account.balance = -200
except AccountException as e:
    print('Exception detected:', e)

try:
    account.number = 'a new one'
except AccountException as e:
    print('Exception detected:', e)

try:
    account.balance += 1_000_000
except AccountException as e:
    print('Exception detected:', e)

try:
    del account.balance
except AccountException as e:
    print('Exception detected:', e)