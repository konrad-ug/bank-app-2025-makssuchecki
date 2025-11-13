from src.personal_account import PersonalAccount


class TestPersonalAccount:
    def test_accepted_condition_one_loan(self):
        account = PersonalAccount("John", "Doe", "00000000000")
        account.balance = 150.0


        account.outgoing_transfer(50.0)

        account.incoming_transfer(10.0)
        account.incoming_transfer(25.0)
        account.incoming_transfer(100.0) 
        
        assert account.submit_for_loan(100.0) == True
        assert account.balance == 335.0

    def test_rejected_condition_one_loan(self):
        account = PersonalAccount("John", "Doe", "00000000000")
        account.balance = 150.0



        account.incoming_transfer(10.0)
        account.incoming_transfer(25.0)
        account.outgoing_transfer(50.0)
        account.incoming_transfer(100.0) 
        
        assert account.submit_for_loan(100.0) == False
        assert account.balance == 235.0


    def test_accepted_condition_two_loan(self):
        account = PersonalAccount("John", "Doe", "00000000000")
        account.balance = 150.0

        account.outgoing_transfer(50.0)
        account.incoming_transfer(50.0)
        account.incoming_transfer(25.0)
        account.outgoing_transfer(25.0)
        account.incoming_transfer(100.0) 
        
        assert account.submit_for_loan(99.0) == True
        assert account.balance == 349.00

    def test_rejected_condition_two_loan(self):
        account = PersonalAccount("John", "Doe", "00000000000")
        account.balance = 150.0

        account.outgoing_transfer(50.0)
        account.incoming_transfer(50.0)
        account.incoming_transfer(25.0)
        account.outgoing_transfer(25.0)
        account.incoming_transfer(100.0) 
        
        assert account.submit_for_loan(101.0) == False
        assert account.balance == 250.0


        