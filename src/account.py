class Account:
    def __init__(self, first_name, last_name, pesel, promo_kod=None):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0.0
        if pesel and len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Invalid"
        self.promo_kod = promo_kod
        
        self.valid_promo()
                
                
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
                    
