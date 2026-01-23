import pytest
import requests
import uuid

class TestAPI:
    url= "http://127.0.0.1:5000/api"
    @pytest.fixture(autouse=True)
    def set_up(self):
        
        all_accounts = requests.get(f"{self.url}/accounts").json()
        for account in all_accounts:
            requests.delete(f"{self.url}/accounts/{account['pesel']}")
    
        payload = {
            "name": "James",
            "surname": "Hetfield",
            "pesel": "89092909825"
        }
        response = requests.post(f"{self.url}/accounts", json=payload)
        assert response.status_code == 201


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

    def test_update_account(self):
        pesel="89092909825"
        update_data={
            "name": "Jimmy",
            "surname": "Hatfold",
            "pesel": "99999999999"
        }
        response = requests.patch(f"{self.url}/accounts/{pesel}", json=update_data)
        assert response.status_code == 200
        assert response.json()["message"] == "Account updated"

    def test_delete_account(self):
        pesel="89092909825"
        response = requests.delete(f"{self.url}/accounts/{pesel}")
        assert response.status_code == 200
        assert response.json()["message"] == "Account deleted"
    

    def test_create_same_pesel_accounts(self):
        url = f"{self.url}/accounts"
        payload = {
            "name": "James",
            "surname": "Hetfield",
            "pesel": "89092909825"
        }
        response = requests.post(url, json=payload)
        assert response.status_code == 409
        assert response.json()['error'] == "Account with such pesel already exists"
        
    
    def test_incoming_transfer(self):
        pesel="89092909825"
        url= f"{self.url}/accounts/{pesel}/transfer"
        payload={
            "amount": 500,
            "type": "incoming"
        }
        response = requests.post(url, json=payload)
        assert response.status_code == 200
        assert response.json()['message'] == "Transfer approved"

    def test_outgoing_transfer(self):
        pesel="89092909825"
        url= f"{self.url}/accounts/{pesel}/transfer"
        
        payload={
            "amount": 1000,
            "type": "incoming"
        }
        requests.post(url, json=payload)

        payload={
            "amount": 500,
            "type": "outgoing"
        }
        response = requests.post(url, json=payload)
        assert response.status_code == 200
        assert response.json()['message'] == "Transfer approved"

    def test_outgoing_error_transfer(self):
        pesel="89092909825"
        url= f"{self.url}/accounts/{pesel}/transfer"
        payload={
            "amount": 500,
            "type": "outgoing"
        }
        response = requests.post(url, json=payload)
        assert response.status_code == 422
        assert response.json()['error'] == "Transfer rejected"

    def test_outgoing_express_transfer(self):
        pesel="89092909825"
        url= f"{self.url}/accounts/{pesel}/transfer"
        
        payload={
            "amount": 1000,
            "type": "incoming"
        }
        requests.post(url, json=payload)

        payload={
            "amount": 500,
            "type": "express"
        }
        response = requests.post(url, json=payload)
        assert response.status_code == 200
        assert response.json()['message'] == "Transfer approved"
        
    def test_outgoing_error_express(self):
        pesel="89092909825"
        url= f"{self.url}/accounts/{pesel}/transfer"
        payload={
            "amount": 500,
            "type": "express"
        }
        response = requests.post(url, json=payload)
        assert response.status_code == 422
        assert response.json()['error'] == "Transfer rejected"
