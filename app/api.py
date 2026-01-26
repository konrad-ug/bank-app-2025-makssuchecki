from flask import Flask, request, jsonify
from src.account_registry import AccountRegistry
from src.personal_account import PersonalAccount
from src.mongo_accounts_repository import MongoAccountsRepository
app = Flask(__name__)
registry = AccountRegistry()

@app.route("/api/accounts", methods=["POST"])
def create_account():
    data = request.get_json()
    print(f"Create account request: {data}")
    
    if registry.search_account_pesel(data["pesel"]) is None: 
        account = PersonalAccount(
            data["name"], 
            data["surname"], 
            data["pesel"])
        registry.add_account(account)
        return jsonify({"message": "Account created"}), 201
    else:
        return jsonify({"error": "Account with such pesel already exists"}), 409

@app.route("/api/accounts", methods=["GET"])
def get_all_accounts():
    print("Get all accounts request received")
    accounts = registry.get_all_accounts()
    accounts_data = [{"name": acc.first_name, "surname": acc.last_name, "pesel":
                       acc.pesel, "balance": acc.balance} for acc in accounts]
    return jsonify(accounts_data), 200

@app.route("/api/accounts/count", methods=["GET"])
def get_account_count():
    print("Get account count request received")
    count = registry.count_accounts()
    return jsonify({"count": count}), 200

@app.route("/api/accounts/<pesel>", methods=["GET"])
def get_account_by_pesel(pesel):
    account = registry.search_account_pesel(pesel)
    if account is None:
        return jsonify({"error": "Account not found"}), 404
        
    return jsonify({"name": account.first_name, "surname": account.last_name, 
                    "pesel": account.pesel, "balance": account.balance }), 200 

@app.route("/api/accounts/<pesel>", methods=["PATCH"])
def update_account(pesel):
    account = registry.search_account_pesel(pesel)
    data = request.get_json()

    if account is None:
        return jsonify({"error": "Account not found"}), 404
    if "name" in data:
        account.first_name = data["name"]
    if "surname" in data:
        account.last_name = data["surname"]
    if "pesel" in data:
        account.pesel = data["pesel"]
        
    return jsonify({"message": "Account updated"}), 200

@app.route("/api/accounts/<pesel>", methods=["DELETE"])
def delete_account(pesel):
    account_deletion = registry.delete_account(pesel)
    if account_deletion:
        return jsonify({"message": "Account deleted"}), 200
    else: 
        return jsonify({"error": "Account not found"}), 404

@app.route("/api/accounts/<pesel>/transfer", methods=["POST"])
def transfer(pesel):
    account = registry.search_account_pesel(pesel)
    
    if account is None:
        return jsonify({"error": "Account not found"}), 404
    
    data = request.get_json()
    
    if "type" not in data or "amount" not in data:
        return jsonify({"error": "Missing fields required"}), 400
    
    transfer_type = data["type"]
    amount = data["amount"]

    if transfer_type == "incoming":
        if not account.incoming_transfer(amount):
            return jsonify({"error": "Invalid amount"}), 422
        return jsonify({"message": "Transfer approved"}), 200

    elif transfer_type == "outgoing":
        if not account.outgoing_transfer(amount):
            return jsonify({"error": "Transfer rejected"}), 422
        return jsonify({"message": "Transfer approved"}), 200

    elif transfer_type == "express":
        if not account.express_outgoing(amount):
            return jsonify({"error": "Transfer rejected"}), 422
        return jsonify({"message": "Transfer approved"}), 200

        
    else:
        return jsonify({"error": "Unknown transfer type"}), 422

@app.route("/api/accounts/save", methods=["PATCH"])
def save_to_db():
    repo = MongoAccountsRepository()
    repo.save_all(registry.get_all_accounts())
    return jsonify({"message": "Accounts saved to a database"}), 200

@app.route("/api/accounts/load", methods=["PATCH"])
def load_from_db():
    repo = MongoAccountsRepository()
    accounts = repo.load_all() or []

    registry.clear()
    for account in accounts:
        registry.add_account(account)

    return jsonify({"message": "Accounts loaded from a database"}), 200