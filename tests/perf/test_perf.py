import requests
import pytest
import random

class TestPerformance:
    url= "http://127.0.0.1:5000/api"
    timeout=0.5

    @pytest.fixture(autouse=True, scope="function")
    def clear(self):
        response = requests.get(f"{self.url}/accounts", timeout=self.timeout)

        for account in response.json():
            pesel = account["pesel"]
            response = requests.delete(f"{self.url}/accounts/{pesel}", timeout=self.timeout)

    def test_create_then_delete_account(self):
        for _ in range(100):
            pesel = ''.join(str(random.randint(0, 9)) for _ in range(11))
            payload = {
                "name": "James",
                "surname": "Hetfield",
                "pesel": pesel
            }

            response = requests.post(f"{self.url}/accounts", json=payload, timeout=self.timeout)
            assert response.status_code == 201

            response = requests.delete(f"{self.url}/accounts/{pesel}", timeout=self.timeout)
            assert response.status_code == 200
    def test_create_then_transfer(self):
        pesel = ''.join(str(random.randint(0, 9)) for _ in range(11))
        payload = {
            "name": "James",
            "surname": "Hetfield",
            "pesel": pesel
        }

        response = requests.post(f"{self.url}/accounts", json=payload)

        for _ in range(100):
            payload_transfer={
                "amount": 500,
                "type": "incoming"
            }
            response = requests.post(f"{self.url}/accounts/{pesel}/transfer", json=payload_transfer, timeout=self.timeout)
            assert response.status_code == 200

