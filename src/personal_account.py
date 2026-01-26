from src.account import Account

class PersonalAccount(Account):
    def __init__(self, first_name, last_name, pesel, promo_kod=None):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        if pesel and len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Invalid"
        self.promo_kod = promo_kod
        
        self.valid_promo()
    def history_prefix(self):
        return "Personal account history"                
                
    def valid_promo(self):
            if self.pesel == "Invalid":
                return 
        
            yy = int(self.pesel[0:2])
            mm = int(self.pesel[2:4])

            if (yy <= 60 and (1 <= mm <= 12)):
                self.balance = 0.0
            else:
                if (self.promo_kod and self.promo_kod.startswith("PROM") and len(self.promo_kod) == len("PROM_XYZ")):
                    self.balance += 50.0

    def express_outgoing(self, amount):
        fee = 1.0
        total_amount = amount + fee
        if (amount > 0 and total_amount <= self.balance + fee):
            self.balance -= total_amount
            self.history.append(f"-{amount}")
            self.history.append(f"-{float(fee)}")
            return True
        else:
            return False

    def condition_one(self):
        last_three = self.history[-3:]
        for i in range(len(last_three)):
            value = float(last_three[i])
            if (value < 0):
                return False
        return True

    def condition_two(self, amount):
        last_five = self.history[-5:]
        total = 0   
        for i in range(len(last_five)):
            value = float(last_five[i])
            total += value  
        return amount < total
        
    def submit_for_loan(self, amount):
        submission = (self.condition_one() or self.condition_two(amount))
        if (submission):
            self.balance += amount
        return submission
    
    def to_dict(self):
        return {
            "name": self.first_name,
            "surname": self.last_name,
            "pesel": self.pesel,
            "balance": self.balance
        }