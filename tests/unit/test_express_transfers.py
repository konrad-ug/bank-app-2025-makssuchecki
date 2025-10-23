from src.account import Account
from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount 

class TestTransfers:
    def test_outgoing_express(self):
        account = PersonalAccount("Alice", "Johnson", "12345678901")
        self.balance = 50.0
        account.express_outgoing(50.0)
        assert account.balance == 0.0
