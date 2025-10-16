class Account:
    def __init__(self, first_name, last_name, pesel, promo_kod=None):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0.0
        if pesel and len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Invalid"

        yy = int(self.pesel[2:])
        mm = int(self.pesel[2:4])
        if ((1 <= mm <= 12) and yy <= 60):
            self.balance = 0.0
        else:
            if (promo_kod and promo_kod.startswith("PROM") and len(promo_kod) == len("PROM_XYZ")):
                self.balance += 50.0
            
            
                