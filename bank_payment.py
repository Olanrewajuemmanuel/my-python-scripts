class BankAccount:
    """
    A class for creating Bank Accounts and neccessary bank methods
    """

    def __init__(self, amount, limit, name):
        self._amount = amount
        self._limit = limit
        self.name = name

    def can_transact(self):
        "If the balance is not lower than the account limit"
        return self._amount >= self._limit

    def __repr__(self):
        return self.name

    def return_acc_balance(self):
        print(self._amount)


class MakeTransfers:
    """
    Make transfers between bank A and bank B
    """
    loan_amount = 100000

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def init_transfer(self, amount):
        if (self.a._amount < amount) or (self.a._amount - amount < amount):
            loan_request = input("{}, Insufficient funds, do you want a loan? \n [y] or [n] \n".format(self.a))
            if loan_request == 'y':
                amount_loaned = amount - self.a._amount
                MakeTransfers.loan_amount -= amount_loaned
                return self.transfer_success(amount)
            elif loan_request == 'n':
                print("Please fund your account to make a transfer")
                return False
            else:
                print("Invalid input")
                return
        return self.transfer_success(amount)

    def transfer_success(self, amount):
        self.a._amount -= amount
        self.b._amount = self.b._amount + amount
        print("{}, Your current balance is {}".format(self.a, self.a._amount))
        print("Transaction successful")


BankA = BankAccount(1000, 100, "Doyin")
BankB = BankAccount(10000, 100, "Lanre")

Transfer = MakeTransfers(BankA, BankB)
Transfer.init_transfer(990)
