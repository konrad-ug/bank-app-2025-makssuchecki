from src.account import Account
from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount 
import pytest
from pytest_mock import MockFixture

@pytest.fixture(autouse=True)
def mock_nip_check(mocker: MockFixture):
    mocker.patch.object(CompanyAccount, "is_nip_active_MF_registry", return_value=True)
    mocker.patch("src.company_account.requests.get")

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
                (100.0, 50.0, 50.0),
                (30.0, 50.0, 30.0),
                (100.0, -20.0, 100.0)
            ]
    )

    def test_outgoing_personal(self, personal_account, balance, amount, expected_personal):
        personal_account.balance = balance
        personal_account.outgoing_transfer(amount)
        assert personal_account.balance == expected_personal



    @pytest.mark.parametrize(
            "balance, amount, expected_company",
            [
                (100.0, 50.0, 50.0),
                (30.0, 50.0, 30.0),
                (100.0, -20.0, 100.0)
            ]
    )
    def test_outgoing_company(self, company_account, balance, amount, expected_company):
        company_account.balance = balance
        company_account.outgoing_transfer(amount)
        assert company_account.balance == expected_company



    @pytest.mark.parametrize(
            "balance, amount, expected",
            [
                (50.0, 100.0, 150.0),
                (50.0, -20.0, 50.0)
            ]
    )
    def test_incoming_personal(self, personal_account, balance, amount, expected):
        personal_account.balance = balance
        personal_account.incoming_transfer(amount)
        assert personal_account.balance == expected


    @pytest.mark.parametrize(
            "balance, amount, expected",
            [
                (50.0, 100.0, 150.0),
                (50.0, -20.0, 50.0)
            ]
    )

    def test_incoming_company(self, company_account, balance, amount, expected):
        company_account.balance = balance
        company_account.incoming_transfer(amount)
        assert company_account.balance == expected

