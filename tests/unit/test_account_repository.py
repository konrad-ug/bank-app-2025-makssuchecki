from src.mongo_accounts_repository import MongoAccountsRepository
import pytest
class TestRepository:
    def test_load_all(self, mocker):
        repo = MongoAccountsRepository()

        mock_collection = mocker.Mock()
        mock_collection.find.return_value = [
            {
                "name": "James",
                "surname": "Hetfield",
                "pesel": "89092909825"
            },
            {
                "name": "Kurt",
                "surname": "Cobain",
                "pesel": "76983512421"
            },
        ]

        repo._collection = mock_collection
        
        accounts = repo.load_all()
        assert len(accounts) == 2
        assert accounts[0].pesel == "89092909825"
        assert accounts[1].first_name == "Kurt"

    def test_save_all(self, mocker):    
        repo = MongoAccountsRepository()

        mock_collection = mocker.Mock()
        repo._collection = mock_collection

        acc1 = mocker.Mock()
        acc1.pesel = "89092909825"
        acc1.to_dict.return_value = {   
            "name": "James",
            "surname": "Hetfield",
            "pesel": "89092909825"
        }
    
        acc2 = mocker.Mock()
        acc2.pesel = "76983512421"
        acc2.to_dict.return_value = {   
            "name": "Kurt",
            "surname": "Cobain",
            "pesel": "76983512421"
        }

        accounts = [acc1, acc2]

        repo.save_all(accounts)

        mock_collection.delete_many.assert_called_once_with({})

        assert mock_collection.update_one.call_count == 2 

        mock_collection.update_one.assert_any_call(
            {"pesel": "89092909825"},
            {"$set": acc1.to_dict.return_value},
            upsert = True
        )