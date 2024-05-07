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
        self._balance = balance
        self._transaction_list = []
        self._transaction_list.append((Account._current_time(), balance))
        print("Account created for " + self._name)
        self.show_balance()
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transaction_list.append((Account._current_time(), amount))
            self.show_balance()
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("Amount to withdraw must be greater than 0 and no more than your account balance")
        self.show_balance()
    
    def show_balance(self):
        print("Balance is {}".format(self._balance))

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
    stephen.deposit(100)
    stephen.withdraw(200)
    stephen.show_transactions()
