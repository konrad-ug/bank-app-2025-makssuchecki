from src.account import Account
from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount

class TestTransferHistory:

    def test_outgoing_person_express(self):
        account = PersonalAccount("Alice", "Johnson", "12345678901")
        account.balance = 150.0

        account.express_outgoing(50.0)

        assert account.history == ["-50.0", "-1"] 

    def test_outgoing_company_express(self):
        account = CompanyAccount("firmex", "1234567890")
        account.balance = 150.0

        account.express_outgoing(50.0)

        assert account.history == ["-50.0", "-5"] 

    def test_outgoing_person(self):
        account = PersonalAccount("Alice", "Johnson", "12345678901")
        account.balance = 150.0

        account.outgoing_transfer(50.0)

        assert account.history == ["-50.0"] 

    def test_outgoing_company(self):
        account = CompanyAccount("firmex", "1234567890")
        account.balance = 150.0

        account.outgoing_transfer(50.0)
        assert account.history == ["-50.0"] 


    def test_incoming_person(self):
        account = PersonalAccount("Alice", "Johnson", "12345678901")
        account.balance = 150.0

        account.incoming_transfer(50.0)

        assert account.history == ["50.0"] 

    def test_incoming_company(self):
        account = CompanyAccount("firmex", "1234567890")
        account.balance = 150.0

        account.incoming_transfer(50.0)

        assert account.history == ["50.0"] 


    def test_incoming_person_express(self):
        account = PersonalAccount("Alice", "Johnson", "12345678901")
        account.balance = 150.0

        account.express_incoming(50.0)

        assert account.history == ["50.0"] 

    def test_incoming_company_express(self):
        account = CompanyAccount("firmex", "1234567890")
        account.balance = 150.0

        account.express_incoming(50.0)

        assert account.history == ["50.0"]


    def test_example_outgoing_person_express(self):
        account = PersonalAccount("Alice", "Johnson", "12345678901")
        account.balance = 150.0

        account.incoming_transfer(500.0)
        account.express_outgoing(300.0)

        assert account.history == ["500.0", "-300.0", "-1"] 

    def test_example_outgoing_company_express(self):
        account = CompanyAccount("firmex", "1234567890")
        account.balance = 150.0

        account.incoming_transfer(500.0)
        account.express_outgoing(300.0)

        assert account.history == ["500.0", "-300.0", "-5"] 


