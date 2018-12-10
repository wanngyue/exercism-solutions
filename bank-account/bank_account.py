from threading import Lock


class BankAccount(object):
    is_open = False
    money = 0
    lock = Lock()

    def __init__(self):
        self.money = 0

    def get_balance(self):
        if self.is_open:
            return self.money
        raise ValueError("Error")

    def open(self):
        if not self.is_open:
            self.is_open = True
        else:
            raise ValueError("Error")

    def deposit(self, amount):
        global money
        if self.is_open and amount > 0:
            self.lock.acquire()
            self.money += amount
            self.lock.release()
        else:
            raise ValueError("Error")

    def withdraw(self, amount):
        global money
        if self.is_open and 0 < amount <= self.money:
            self.lock.acquire()
            self.money -= amount
            self.lock.release()
        else:
            raise ValueError("Error")

    def close(self):
        if self.is_open:
            self.is_open = False
            self.money = 0
        else:
            raise ValueError("Error")
