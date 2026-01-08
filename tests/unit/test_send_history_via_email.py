from pytest_mock import MockFixture
from src.company_account import CompanyAccount
from src.personal_account import PersonalAccount
from src.account import Account
import pytest

class TestSendHistoryViaEmail:
    def test_personal_account_send_email(self, mocker: MockFixture):
        mock_send = mocker.patch("src.account.SMTPClient.send", return_value=True)

        account = PersonalAccount("Jan", "Kowalski", "90010112345")
        account.history = [100, -1, 500]

        result = account.send_history_via_email("test@example.com")

        assert result is True
        mock_send.assert_called_once()

        subject, text, email = mock_send.call_args[0]
        assert subject.startswith("Account Transfer History")
        assert text == "Personal account history: [100, -1, 500]"
        assert email == "test@example.com"

    def test_personal_account_send_history_failure(self, mocker: MockFixture):
        mocker.patch("src.account.SMTPClient.send", return_value=False)

        account = PersonalAccount("Jan", "Kowalski", "90010112345")
        result = account.send_history_via_email("test@example.com")

        assert result is False

    def test_company_account_send_email(self, mocker: MockFixture):
        mock_send = mocker.patch("src.account.SMTPClient.send", return_value=True)
        mock = mocker.patch("src.company_account.requests.get")
        mock.return_value.status_code = 200
        mock.return_value.json.return_value = {"result": {"subject": {"statusVat": "Czynny"}}}
        
        account = CompanyAccount("Tech Solutions", "8461627562")
        account.history = [100, -1, 500]

        result = account.send_history_via_email("test@example.com")

        assert result is True
        mock_send.assert_called_once()

        subject, text, email = mock_send.call_args[0]
        assert subject.startswith("Account Transfer History")
        assert text == "Company account history: [100, -1, 500]"
        assert email == "test@example.com"

    def test_company_account_send_history_failure(self, mocker: MockFixture):
        mocker.patch("src.account.SMTPClient.send", return_value=False)
        mock = mocker.patch("src.company_account.requests.get")
        mock.return_value.status_code = 200
        mock.return_value.json.return_value = {"result": {"subject": {"statusVat": "Czynny"}}}
        
        account = CompanyAccount("Tech Corp", "8461627562")
        result = account.send_history_via_email("firma@example.com")

        assert result is False