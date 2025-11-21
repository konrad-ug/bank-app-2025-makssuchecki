from src.company_account import CompanyAccount
import pytest

class TestCompanyAccount:
    @pytest.fixture
    def make_company_account(self):
        def make(name, nip):
            return CompanyAccount(name, nip)
        return make

    @pytest.mark.parametrize(
            "name, nip, expected",
            [
                ("metalex", "99999", "Invalid"),
                ("firmex", "444444444444444", "Invalid"),
                ("budix", "", "Invalid"),
                ("budix", "ewfwfe", "Invalid"),
                ("firma", "1234567890", "1234567890"),
            ]
    )
    def test_nip(self, make_company_account, name, nip, expected):
        account = make_company_account(name, nip)
        assert account.nip == expected

    def test_account_creation(self, make_company_account):
        account = make_company_account("metalex", "1234567890")
        assert account.company_name == "metalex"
        assert account.nip == "1234567890"
        assert account.balance == 0.0
