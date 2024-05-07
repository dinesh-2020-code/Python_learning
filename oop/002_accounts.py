import datetime
import pytz


class Account:
    """Simple Account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = []
        self._transaction_list.append((Account._current_time(), balance))
        print("Account created for " + self._name)
        self.show_balance()
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._transaction_list.append((Account._current_time(), amount))
            self.show_balance()
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("Amount to withdraw must be greater than 0 and no more than your account balance")
        self.show_balance()
    
    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount >= 0:
                tran_type = "deposition"
            else:
                tran_type = "withdrawal"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == "__main__":
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    # tim.show_balance()
    tim.withdraw(400)
    # tim.show_balance()
    tim.withdraw(2000)
    tim.show_transactions()
    # tim.show_balance()

    stephen = Account("Stephen", 800)
    stephen.__balance = 200   # Names are only mangled when they start with two underscores and no more than a single underscore
    stephen.deposit(100)
    stephen.withdraw(200)
    stephen.show_transactions()
    print(stephen.__dict__)
    # stephen._Account__balance = 40
    # stephen.show_balance()
    # print(stephen.__dict__)
