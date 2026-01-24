from pymongo import MongoClient
from src.personal_account import PersonalAccount

class MongoAccountsRepository:
    def __init__(self, uri="mongodb://localhost:27017"):
        self._client = MongoClient()
        db = self._client["bank_db"]
        self._collection = db["accounts"]
 
    def save_all(self, accounts):
        self._collection.delete_many({})
        for account in accounts:
            self._collection.update_one(
                {"pesel": account.pesel},
                {"$set": account.to_dict()},
                upsert=True,
            )

    def load_all(self):
        documents = self._collection.find()

        accounts = []
        for doc in documents:
            account = PersonalAccount(
                doc["name"],
                doc["surname"],
                doc["pesel"]
            )
            accounts.append(account)
        return accounts