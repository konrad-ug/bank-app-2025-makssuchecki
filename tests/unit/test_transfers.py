from src.account import Account
from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount 
import pytest

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

