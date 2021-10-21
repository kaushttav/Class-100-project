class Atm(object):
    def __init__(self, atmCardNumber, pinNumber, name, currency, money_in_bank):
        self.atmCardNumber = atmCardNumber
        self.pinNumber = pinNumber
        self.name = name
        self.currency = currency
        self.money_in_bank = money_in_bank

    def cashWithdrawal(self):
        cash = int(input("Enter the amount that you want to withdraw (in " + self.currency + "): "))
        print("Dear " + self.name + ", " + self.currency, cash, " withdrawn!")
        self.money_in_bank = self.money_in_bank - cash
    
    def balanceEnquiry(self):
        print("You have " + self.currency, self.money_in_bank, "in the bank.")

    def getInfo(self):
        print("Name: " + self.name)
        print("ATM Card Number:", self.atmCardNumber)
        print("PIN Number:", self.pinNumber)
        print("Currency in your country: " + self.currency)
        print("Money in the bank:", self.money_in_bank)

user1 = atm(123456789, 54321, "Karan", "Rs.", 10000)
user1.getInfo()
user1.cashWithdrawal()
user1.balanceEnquiry()

user2 = atm(987654321, 65432, "Hito", "$", 14000)
user2.getInfo()
user2.cashWithdrawal()
user2.balanceEnquiry()