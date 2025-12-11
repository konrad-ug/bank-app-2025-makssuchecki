from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount
import pytest
from pytest_mock import MockFixture

@pytest.fixture(autouse=True)
def mock_nip_check(mocker: MockFixture):
    mocker.patch.object(CompanyAccount, "is_nip_active_MF_registry", return_value=True)
class TestTransferHistory:
    @pytest.fixture(params=["personal", "company"])
    def account(self, request):
        if request.param == "personal":
            acc = PersonalAccount("John", "Doe", "12345678901")
        else:
            acc = CompanyAccount("Firmex", "1234567890")
        acc.balance = 150.0
        return acc

    @pytest.mark.parametrize(
            "amount, expected_history",
            [
                (50.0, ["-50.0"]),
            ]
    )
    def test_outgoing(self, account, amount, expected_history):
        account.outgoing_transfer(amount)
        assert account.history == expected_history

    @pytest.mark.parametrize(
            "amount, expected_personal, expected_company",
            [
                (50.0, ["-50.0", "-1.0"], ["-50.0", "-5.0"]),
            ]
    )
    def test_outgoing_express(self, account, amount, expected_personal, expected_company):
        account.express_outgoing(amount)
        if isinstance(account, PersonalAccount):
            assert account.history == expected_personal
        else:
            assert account.history == expected_company


    @pytest.mark.parametrize(
            "amount, expected_history",
            [
                (50.0, ["50.0"]),
            ]
    )

    def test_incoming(self, account, amount, expected_history):
        account.incoming_transfer(amount)
        assert account.history == expected_history

    @pytest.mark.parametrize(
            "inc, out, expected_personal, expected_company",
            [
                (500.0, 300.0, ["500.0", "-300.0", "-1.0"], ["500.0", "-300.0", "-5.0"]),
            ]
    )        
    def test_inc_out(self, account, inc, out, expected_personal, expected_company):
        account.incoming_transfer(inc)
        account.express_outgoing(out)

        if isinstance(account, PersonalAccount):
            assert account.history == expected_personal
        else:
            assert account.history == expected_company


''' Old version of tests
    def test_outgoing_person_express(self):
        account = PersonalAccount("Alice", "Johnson", "12345678901")
        account.balance = 150.0

        account.express_outgoing(50.0)

        assert account.history == ["-50.0", "-1"] 

    def test_outgoing_company_express(self):
        account = CompanyAccount("firmex", "1234567890")
        account.balance = 150.0

        account.express_outgoing(50.0)

        assert account.history == ["-50.0", "-5"] 

    def test_outgoing_person(self):
        account = PersonalAccount("Alice", "Johnson", "12345678901")
        account.balance = 150.0

        account.outgoing_transfer(50.0)

        assert account.history == ["-50.0"] 

    def test_outgoing_company(self):
        account = CompanyAccount("firmex", "1234567890")
        account.balance = 150.0

        account.outgoing_transfer(50.0)
        assert account.history == ["-50.0"] 


    def test_incoming_person(self):
        account = PersonalAccount("Alice", "Johnson", "12345678901")
        account.balance = 150.0

        account.incoming_transfer(50.0)

        assert account.history == ["50.0"] 

    def test_incoming_company(self):
        account = CompanyAccount("firmex", "1234567890")
        account.balance = 150.0

        account.incoming_transfer(50.0)

        assert account.history == ["50.0"] 


    def test_incoming_person_express(self):
        account = PersonalAccount("Alice", "Johnson", "12345678901")
        account.balance = 150.0

        account.express_incoming(50.0)

        assert account.history == ["50.0"] 

    def test_incoming_company_express(self):
        account = CompanyAccount("firmex", "1234567890")
        account.balance = 150.0

        account.express_incoming(50.0)

        assert account.history == ["50.0"]


    def test_example_outgoing_person_express(self):
        account = PersonalAccount("Alice", "Johnson", "12345678901")
        account.balance = 150.0

        account.incoming_transfer(500.0)
        account.express_outgoing(300.0)

        assert account.history == ["500.0", "-300.0", "-1"] 

    def test_example_outgoing_company_express(self):
        account = CompanyAccount("firmex", "1234567890")
        account.balance = 150.0

        account.incoming_transfer(500.0)
        account.express_outgoing(300.0)

        assert account.history == ["500.0", "-300.0", "-5"] 


'''