from src.account import Account

class CompanyAccount(Account):
    def __init__(self, company_name, nip):
        super().__init__()
        self.company_name = company_name
        if (len(nip) != 10):
            self.nip = "Invalid" 
        else:
            self.nip = nip