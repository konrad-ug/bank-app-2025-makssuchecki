from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount 
import pytest
from pytest_mock import MockFixture


@pytest.fixture(autouse=True)
def mock_nip_check(mocker: MockFixture):
    mocker.patch.object(CompanyAccount, "is_nip_active_MF_registry", return_value=True)
class TestTransfers:
    @pytest.fixture()
    def personal_account(self):
        return PersonalAccount("John", "Doe", "00000000000")
    
    @pytest.fixture()
    def company_account(self):
        return CompanyAccount("Firmex", "1234567890")
    
    @pytest.mark.parametrize(
            "balance, amount, expected_personal",
            [
                (150.0, 50.0, 99.0),
                (50.0, 50.0, -1.0),
            ]
    )

    def test_express_outgoing_personal(self, personal_account, balance, amount, expected_personal):
        personal_account.balance = balance
        personal_account.express_outgoing(amount)
        assert personal_account.balance == expected_personal

    @pytest.mark.parametrize(
            "balance, amount, expected_company",
            [
                (150.0, 50.0, 95.0),
                (50.0, 50.0, -5.0),
            ]
    )

    def test_express_outgoing_company(self, company_account, balance, amount, expected_company):
        company_account.balance = balance
        company_account.express_outgoing(amount)
        assert company_account.balance == expected_company

    @pytest.mark.parametrize(
            "balance, amount, expected",
            [
                (100.0, 50.0, 150.0),
            ]
    )

    def test_express_incoming_company(self, company_account, balance, amount, expected):
        company_account.balance = balance
        company_account.express_incoming(amount)
        assert company_account.balance == expected
    @pytest.mark.parametrize(
            "balance, amount, expected",
            [
                (100.0, 50.0, 150.0),
            ]
    )
    def test_express_incoming_personal(self, personal_account, balance, amount, expected):
        personal_account.balance = balance
        personal_account.express_incoming(amount)
        assert personal_account.balance == expected


''' Older version of tests
    def test_outgoing_personal_express(self):
        self.personal_account.balance = 150.0
        self.personal_account.express_outgoing(50.0)
        assert self.personal_account.balance == 99.0

    def test_outgoing_company_express(self):
        self.company_account.balance = 150.0
        self.company_account.express_outgoing(50.0)
        assert self.company_account.balance == 95.0


    def test_outgoing_debit_personal_express(self):
        self.personal_account.balance = 50.0
        self.personal_account.express_outgoing(50.0)
        assert self.personal_account.balance == -1.0

    def test_outgoing_debit_company_express(self):
        self.company_account.balance = 50.0
        self.company_account.express_outgoing(50.0)
        assert self.company_account.balance == -5.0

    def test_incoming_personal_express(self):
        account = PersonalAccount("Alice", "Johnson", "12345678901")
        account.balance = 100.0
        account.express_incoming(50.0)
        assert account.balance == 150.0


    def test_incoming_company_express(self):
        account = CompanyAccount("firmex", "1234567899")
        account.balance = 100.0
        account.express_incoming(50.0)
        assert account.balance == 150.0
'''