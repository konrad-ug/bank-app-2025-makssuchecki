from src.personal_account import PersonalAccount
import pytest

class TestPersonalAccount:
    @pytest.fixture
    def make_personal_account(self):
        def make(first_name, last_name, pesel, promo=None):
            return PersonalAccount(first_name, last_name, pesel, promo)
        return make

    @pytest.mark.parametrize(
            "first_name, last_name, pesel, expected",
            [
                ("John", "Doe", "12345", "Invalid"),
                ("John", "Doe", "12345123451234512345", "Invalid"),
                ("John", "Doe", None, "Invalid"),
            ]
    )

    def test_pesel(self, make_personal_account, first_name, last_name, pesel, expected):
        account = make_personal_account(first_name, last_name, pesel)
        assert account.pesel == expected
        
    def test_account_creation(self, make_personal_account):
        account = make_personal_account("John", "Doe", "00000000000")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.0
        assert account.pesel == "00000000000"

    @pytest.mark.parametrize(
            "pesel, promo, expected",
            [
                ("79530000000", "PROM_ABC", 50.0),
                ("00000000000", "KODY_XYS", 0.0),
                ("00000000000", "KODY", 0.0),
                ("60011111111", "PROM_KOD", 0.0),
                ("04290000000", "PROM_KOD", 50.0),
            ]
    )
    def test_promo(self, make_personal_account, pesel, promo, expected):
        account = make_personal_account("John", "Doe", pesel, promo)
        assert account.balance == expected
