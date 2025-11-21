from src.personal_account import PersonalAccount
import pytest

class TestPersonalAccount:
    @pytest.fixture(autouse=True, scope="function")
    def account(self):
        self.account = PersonalAccount("John", "Doe", "00000000000")

    @pytest.mark.parametrize(
            "history, expected, amount",
            [
                (["-50.0", "10.0", "25.0", "100.0"], True, 100.0),
                (["50", "10.0", "-25.0", "50.0"], False, 100.0),
                (["-50.0", "50.0", "-25.0", "25.0", "100.0"], True, 99.0),
                (["-50.0", "50.0", "-25.0", "25.0", "100.0"], False, 101.0)
            ]
    )

    def test_loan_parametrize(self, history, expected, amount):
        self.account.history = history
        assert self.account.submit_for_loan(amount) == expected


''' Testy bez użycia fixture i parametrize
    def test_accepted_condition_one_loan(self):
        self.account.history = ["-50.0", "10.0", "25.0", "100.0"]
        self.account.balance == 150.0

        assert self.account.submit_for_loan(100.0) == True

    def test_rejected_condition_one_loan(self):
        self.account.history = ["50", "10.0", "-25.0", "50.0"]
        self.account.balance == 150.0

        assert self.account.submit_for_loan(100.0) == False


    def test_accepted_condition_two_loan(self):
        self.account.history = ["-50.0", "50.0", "-25.0", "25.0", "100.0"]
        self.account.balance == 150.0

        assert self.account.submit_for_loan(99.0) == True

    def test_rejected_condition_two_loan(self):
        self.account.history = ["-50.0", "50.0", "-25.0", "25.0", "100.0"]
        self.account.balance == 150.0

        assert self.account.submit_for_loan(101.0) == False
'''