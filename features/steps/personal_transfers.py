from behave import *
import requests

URL = "http://localhost:5000"

@given('a personal account with pesel "{pesel}" and balance of {balance:d}')
def step_given_account_with_balance(context, pesel, balance):
    requests.delete(URL + f"/api/accounts/{pesel}")
    json_body = {"name": "user",
                 "surname": "test",
                 "pesel": pesel,
    } 
    create_resp = requests.post(URL + "/api/accounts", json = json_body)
    assert create_resp.status_code == 201
    if balance > 0:
        response = requests.post(URL + f"/api/accounts/{pesel}/transfer",
                                 json={
                                     "amount": balance,
                                     "type": "incoming"
                                })
        assert response.status_code == 200
    
    context.pesel = pesel
    context.last_transfer_response = None

@when("an incoming transfer of {amount:d} is credited to the account")
def step_when_incoming_transfer(context, amount):
    response = requests.post(URL + f"/api/accounts/{context.pesel}/transfer", 
                             json={
                                 "type": "incoming",
                                 "amount": amount
                             })
    context.last_transfer_response = response

@when("an outgoing transfer of {amount:d} is executed")
def step_when_outgoing_transfer(context, amount):
    response = requests.post(URL + f"/api/accounts/{context.pesel}/transfer", 
                             json={
                                 "type": "outgoing",
                                 "amount": amount
                             })
    context.last_transfer_response = response

@then("the account balance should be {expected_balance:d}")
def step_then_account_balance(context, expected_balance):
    response = requests.get(URL + f"/api/accounts/{context.pesel}")
    assert response.status_code == 200

    data = response.json()
    assert data["balance"] == expected_balance

@then("the transfer should be rejected")
def step_then_transfer_rejected(context):
    assert context.last_transfer_response is not None
    assert context.last_transfer_response.status_code in (400, 422)