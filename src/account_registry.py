from src.personal_account import PersonalAccount
from typing import List

class AccountRegistry:
    def __init__(self):
        self.accounts: List[PersonalAccount] = []

    def add_account(self, account: PersonalAccount):
        self.accounts.append(account)

    def search_account_pesel(self, pesel):
        for account in self.accounts:
            if account.pesel == pesel:
                return account
        return None
            
    def all_accounts(self):
        return self.accounts
    
    def count_accounts(self):
        return len(self.accounts)