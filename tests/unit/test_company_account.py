from pytest_mock import MockFixture
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
            ]
    )
    def test_nip(self, make_company_account, name, nip, expected):
        account = make_company_account(name, nip)
        assert account.nip == expected

    def test_company_account_creation(self, mocker: MockFixture):
        # mocker.patch.object(CompanyAccount, "is_nip_active_MF_registry", return_value=True)
        mock = mocker.patch("requests.get")
        mock.return_value.status_code = 200
        mock.return_value.json.return_value = {"result": {"subject": {"statusVat": "Czynny"}}}
        company_account = CompanyAccount("Tech Solutions", "8461627562")
        assert company_account.name == "Tech Solutions"
        assert company_account.balance == 0.0
        assert company_account.nip == "8461627562"
