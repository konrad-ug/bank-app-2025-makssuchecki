from src.account import Account
from flask import Flask, request, jsonify
from datetime import datetime
import requests
import os

class CompanyAccount(Account):
    BANK_APP_MF_URL = os.getenv("BANK_APP_MF_URL", "https://wl-test.mf.gov.pl/")
    def __init__(self, company_name, nip):
        super().__init__()
        self.company_name = company_name
        if not self.is_nip_valid(nip):
            self.nip = "Invalid"
        elif self.is_nip_active_MF_registry(nip):
            self.nip = nip
        else:
            raise ValueError("Company not registered!") 
    
    def is_nip_valid(self, nip):
        if (isinstance(nip, str) and len(nip) == 10 and nip.isdigit()):
            return True
        return False

    def express_outgoing(self, amount):
        fee = 5.0
        total_amount = amount + fee
        if (amount > 0 and total_amount <= self.balance + fee):
            self.balance -= total_amount
            self.history.append(f"-{amount}")
            self.history.append(f"-{(fee)}")


    def paid_zus(self):
        if ("-1775" in self.history):
            return True
        return False
        
    def take_loan(self, amount):
        if (self.balance >= (2*amount) and self.paid_zus()):
            self.balance += amount
            return True
        return False 
        
    def is_nip_active_MF_registry(self, nip):
        today_date = datetime.today().strftime("%Y-%m-%d")
        url = f"{self.BANK_APP_MF_URL}api/search/nip/{nip}?date={today_date}"
        
        print(f"Sending requests to {url}")
        response = requests.get(url)
        print(f"Response status code: {response.json()}")
        
        if response.status_code != 200:
            return False

        data = response.json() or {}
        result = data.get("result") or {}
        subject = result.get("subject") or {}
        status = subject.get("statusVat")

        return status == "Czynny"