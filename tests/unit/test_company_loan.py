from src.company_account import CompanyAccount
import pytest
from pytest_mock import MockFixture


@pytest.fixture(autouse=True)
def mock_nip_check(mocker: MockFixture):
    mocker.patch.object(CompanyAccount, "is_nip_active_MF_registry", return_value=True)


class TestCompanyLoan:

    @pytest.fixture(autouse=True)
    def account(self):
        self.account = CompanyAccount("Tech Solutions", "8461627562")

    @pytest.mark.parametrize(
        "history, expected, amount, balance",
        [
            (["50", "-1775", "100", "24", "-532"], True, 200.0, 400.0),
            (["540", "11", "2124", "1775"], False, 200.0, 1010.0),
            (["540", "11", "2124", "-1775"], False, 200.0, 399.0),
        ]
    )
    def test_company_loan_parametrize(self, history, expected, amount, balance):
        self.account.history = history
        self.account.balance = balance
        assert self.account.take_loan(amount) == expected