from Account import Account

class Customer:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.accounts = []

    def __str__(self):
        return f"{self.username}/{self.password}"

    def __repr__(self):
        return f"Username: {self.username} / Password: {self.password} "

    def add_account(self, account_number, balance):
        account = Account(account_number, balance)
        self.accounts.append(account)

    def change_password(self, new_password):
        self.password = new_password