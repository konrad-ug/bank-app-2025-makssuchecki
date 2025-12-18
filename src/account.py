from datetime import datetime
from src.lib.smtp import SMTPClient

class Account:
    def __init__(self):
        self.balance = 0.0
        self.history = []

    def outgoing_transfer(self, amount: float) -> None:
        if (amount < self.balance and amount > 0.0):
            self.balance -= amount
            self.history.append(f"-{amount}")
            return True
        else:
            return False

    def incoming_transfer(self, amount: float) -> None:
        if (amount > 0.0 ):
            self.balance += amount
            self.history.append(f"{amount}")


    def express_incoming(self, amount: float) -> None:
        if (amount > 0.0 ):
            self.balance += amount
            self.history.append(f"{amount}")

    def send_history_via_email(self, email_adress: str) -> bool:
        today_date = datetime.today().strftime("%Y-%m-%d")
        subject = f"Account Transfer History {today_date}"
        text = f"{self.history_prefix()}: {self.history}"

        
        smtp = SMTPClient()
        return smtp.send(subject, text, email_adress)
    