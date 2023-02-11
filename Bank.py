from Customer import Customer
import json

class BankingFunctions:
    def __init__(self):
        self.customers = []
        self.current_user = None

    def __str__(self):
        return f"Logged in user: {self.current_user}"

    def add_customer(self,username, password): #working
        customer = Customer(username, password)
        self.customers.append(customer)
        return print("Congratulations for signing up.")

    def get_customer(self, username): #working
        for customer in self.customers:
            if customer.username == username:
                return customer
        raise ValueError("Customer not found")

    def remove_customer(self, username): #working
        customer = self.get_customer(username)
        self.customers.remove(customer)
        return print("Successfully removed customer.")

    def get_customers(self): #working
        return self.customers

    def add_account(self, customer, account_number, balance): #working
        customer.add_account(account_number, balance)
        return print("Successfully created account.")

    def get_account(self, customer, account_number): #working
        for account in customer.accounts:
            if account.account_number == account_number:
                return account
        return print("No account found.")

    def remove_account(self, customer, account_number): #working
        account = self.get_account(customer, account_number)
        customer.accounts.remove(account)
        return print("Successfully removed account.")

    def get_accounts(self, customer): #working
        return customer.accounts

    def deposit(self, account, amount): #working
        account.balance += amount
        return print("Successfully deposited amount.")

    def withdraw(self, account, amount): #working
        if account.balance < amount:
            return print("Insufficient funds.")
        account.balance -= amount
        return print("Successfully withdrew amount.")

    def get_all_balances(self, customer): #working
        balances = []
        for account in customer.accounts:
            balances.append(account.balance)
        return balances

    def login(self, username, password): #working
        for customer in self.customers:
            if customer.username == username and customer.password == password:
                self.current_user = customer
                print("Successfully logged in.")
                return customer
        return print("Invalid username or password")

    def logout(self): #working
        self.current_user = None
        return print("User has been logged out.")

    def change_password(self, username, new_password): #working
        customer = self.get_customer(username)
        customer.change_password(new_password)

    def check_logged_in_user(self): #working
        if self.current_user is None:
            return print("No user is logged in.")
        return self.current_user

    def print_user_accounts(self, customer): #working
        for account in customer.accounts:
            print("Account Number:", account.account_number, " / Balance:", account.balance)

    def print_all_customers(self): #working
        for customer in self.customers:
            print("Username:", customer.username)

    def print_to_txt(self,filename): #working
        with open(f"{filename}", "w") as file:
            for customer in self.customers:
                file.write(str(customer) + "#")

                for account in customer.accounts:
                    file.write(str(account) + "@")
                file.write("\n")
        return print(f"Successfully printed file to {filename}")
##text
    def read_from_txt(self, file_name): #working!
        with open(file_name, "r") as file:
            for line in file:
                customer_data = line.strip().split("#")
                customer_info = customer_data[0]
                account_data = customer_data[1].rstrip("@")
                user_log_in_info = customer_data[0].strip().split("/")
                username = user_log_in_info[0]
                password = user_log_in_info[1]
                account_numbers = []
                balances = []
                for accounts in account_data.strip().split('@'):
                    account_info = accounts.strip().split('/')
                    if account_info == None:
                        print("Done")
                    account_number = account_info[0]
                    account_balance = account_info[1]
                    account_numbers.append(account_number)
                    balances.append(account_balance)
                print("\nusername:", username)
                print("password:", password)
                print("accounts:", account_numbers)
                print("balances:", balances)
            return username, password, account_numbers, balances

    def load_data_from_txt(self, file_name): #working!
        with open(file_name, 'r') as file:
            for line in file:
                line = line.rstrip('\n')
                if line[-1] == '@':
                    line = line[:-1]
                username, user_data = line.split('/', 1)
                password, accounts_data = user_data.split('#', 1)
                customer = Customer(username, password)
                self.customers.append(customer)
                for account_data in accounts_data.split('@'):
                    account_info = account_data.split('/')
                    account_number = account_info[0]
                    balance = account_info[1]
                    account = customer.add_account(account_number, balance)
                    customer.add_account(account, balance)
        return print(f"Successfully loaded {file_name}")


##json

    def data_to_dict(self): #working
        data = {"customers": []}
        for customer in self.customers:
            customer_data = {"username": customer.username, "password": customer.password, "accounts": []}
            for account in customer.accounts:
                customer_data["accounts"].append({"account_number": account.account_number, "balance": account.balance})
            data["customers"].append(customer_data)
        return data

    def save_data_to_json(self, file_name): #working
        data = self.data_to_dict()
        with open(file_name, 'w') as file:
            json.dump(data, file)
        return print(f"Successfully saved to {file_name} ")

    def load_data_from_json(self, file_name): #working
        with open(file_name, 'r') as file:
            data = json.load(file)
        for customer_data in data["customers"]:
            customer = Customer(customer_data["username"], customer_data["password"])
            for account_data in customer_data["accounts"]:
                customer.add_account(account_data["account_number"], account_data["balance"])
            self.customers.append(customer)
        return print(f"Successfully loaded data from {file_name}")
