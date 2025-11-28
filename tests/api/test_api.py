import pytest
import requests


class TestAPI:
    url= "http://127.0.0.1:5000/api"
    @pytest.fixture(autouse=True)
    def set_up(self):
        url = f"{self.url}/accounts"
        payload = {
            "name": "James",
            "surname": "Hetfield",
            "pesel": "89092909825"
        }
        response = requests.post(url, json=payload)
        assert response.status_code == 201
        yield
        all_accounts = requests.get(f"{self.url}/accounts").json()
        for account in all_accounts:
            requests.delete(f"{self.url}/accounts/{account['pesel']}")


    def test_create_accounts(self):
        url = f"{self.url}/accounts"
        payload = {
            "name": "James",
            "surname": "Hetfield",
            "pesel": "89092909825"
        }
        response = requests.post(url, json=payload)
        assert response.status_code == 201
        assert response.json()['message'] == "Account created"

    def test_get_account_count(self):
        url = f"{self.url}/accounts/count"
        response = requests.get(url)

        assert response.status_code == 200
        assert response.json()["count"] == 1

    def test_search_by_pesel(self):
        pesel = "89092909825"
        url = f"{self.url}/accounts/{pesel}"
        response = requests.get(url)

        assert response.status_code == 200
        assert response.json()["name"] == "James"


    def test_missing_account(self):
        pesel = "00000000000"
        url = f"{self.url}/accounts/{pesel}"
        response = requests.get(url)
        
        assert response.status_code == 404
