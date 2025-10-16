from src.account import Account


class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe", "00000000000")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.0
        assert account.pesel == "00000000000"

    def test_pesel_too_short(self):
        account = Account("John", "Doe", "12345")
        assert account.pesel == "Invalid"
    def test_pesel_too_long(self):
        account = Account("John", "Doe", "12345123451234512345")
        assert account.pesel == "Invalid"
    def test_pesel_none(self):
        account = Account("John", "Doe", None)
        assert account.pesel == "Invalid"

    def test_correct_promo(self):
        account = Account("John", "Doe", "79530000000", "PROM_ABC")
        assert account.balance == 50.0
    def test_wrong_promo(self):
        account = Account("John", "Doe", "00000000000", "KODY_XYS")
        assert account.balance == 0.0
    def test_too_short_promo(self):
        account = Account("John", "Doe", "00000000000", "KODY")
        assert account.balance == 0.0

    def test_senior_nopromo(self):
        account = Account("John", "Doe", "60010000000", "PROM_KOD")
        assert account.balance == 0.0
    def test_notseenior_promo(self):
        account = Account("John", "Doe", "04290000000", "PROM_KOD")
        assert account.balance == 50.0