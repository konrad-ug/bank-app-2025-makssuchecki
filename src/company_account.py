from src.account import Account

class CompanyAccount(Account):
    def __init__(self, company_name, nip):
        super().__init__()
        self.company_name = company_name
        if (len(nip) != 10):
            self.nip = "Invalid" 
        else:
            self.nip = nip

    def express_outgoing(self, amount):
        fee = 5.0
        total_amount = amount + fee
        if (amount > 0 and total_amount <= self.balance + fee):
            self.balance -= total_amount
            self.history.append(f"-{amount}")
            self.history.append(f"-{(fee)}")


    def paid_zus(self):
        if ("-1775" in self.history):
            return True
        return False
        
    def take_loan(self, amount):
        if (self.balance >= (2*amount) and self.paid_zus()):
            self.balance += amount
            return True
        return False 
        
            