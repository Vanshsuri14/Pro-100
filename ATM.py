class ATM(object):
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def cashWithdrawl(self):
        print("cash is withdrawl")

person1 = ATM("128920893456","3067")

person1.cashWithdrawl()