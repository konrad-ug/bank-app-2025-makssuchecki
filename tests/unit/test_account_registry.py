from src.account_registry import AccountRegistry
from src.personal_account import PersonalAccount
import pytest

class TestAccountRegistry:
    @pytest.fixture()
    def registry(self):
        return AccountRegistry()

    def test_add_and_search(self, registry: AccountRegistry):
        account = PersonalAccount("John", "Doe", "12532632532")
        registry.add_account(account)
        get_account = registry.search_account_pesel("12532632532")
        assert get_account == account

    def test_add_and_search_not_found(self, registry: AccountRegistry):
        get_account = registry.search_account_pesel("12532632532")
        assert get_account is None

    def test_get_all_accounts(self, registry: AccountRegistry):
        account1 = PersonalAccount("John", "Doe", "12532632532")
        account2 = PersonalAccount("Jane", "Day", "99887766553")
        registry.add_account(account1)
        registry.add_account(account2)
        all_accounts = registry.all_accounts()
        assert all_accounts == [account1, account2]

    def test_accounts_count(self, registry: AccountRegistry):
        account1 = PersonalAccount("John", "Doe", "12532632532")
        account2 = PersonalAccount("Jane", "Day", "99887766553")
        registry.add_account(account1)
        registry.add_account(account2)
        count_accounts = registry.count_accounts()
        assert count_accounts == 2
