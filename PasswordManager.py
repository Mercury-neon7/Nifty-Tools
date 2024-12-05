class PasswordManager():

    def __init__(self):
        self.accounts = {}

    def add_account(self, website, username, password):
        if website in self.accounts:
            self.accounts[website].append({"username": username, "password": password})
            print(f'account appended to {website}')
        else:
            self.accounts[website] = ({"username": username, "password": password})
            print(f'account created to {website}')

    def add_account(self, website, username, password):
        if website in self.accounts:
            self.accounts[website].append({"username": username, "password": password})
            print(f"{username} succesfully appended to {website}")
        else:
            self.accounts[website] = [{"username": username, "password": password}]
            print(f"{website} succesfully created")

    def remove_account(self, website):
        if website not in self.accounts:
            print("website doesn't exist")
            return
        
        accounts = self.accounts[website]
        if len(accounts) == 1:
            confirm = input(f"do you really want to delete this account for {website}? (yes/no)").lower()
            if confirm == "yes":
                del self.accounts[website]
                print(f"{website} succesfully deleted")
            else:
                print("Deletion cancelled")
        else:
            print(f"accounts for {website}")
            for i, account in enumerate(accounts, start=1):
                print(f"{i}. Username: {account['username']}, Password: {account['password']}")
            
            try:
                choice = int(input("Enter the number of the account you want to delete: "))
                if 1 <= choice <= len(accounts):
                    accounts.pop(choice - 1)
                    print("Account deleted.")
                    if not accounts:
                        del self.accounts[website]
                else:
                    print("Invalid choice.")
            except ValueError:
                print("invalid input")

    def display_info(self):
        if not self.accounts:
            print("No accounts stored")
        else:
            for website, credentials_list in self.accounts.items():
                print(f"Website: {website}")
                for credentials in credentials_list:
                    print(f"  Username: {credentials['username']}, Password: {credentials['password']}")
