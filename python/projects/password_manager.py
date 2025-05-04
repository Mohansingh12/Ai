class PasswordManager:
    def __init__(self):
        self.passwords = {'google.com': {'username': 'user1', 'password': 'pass1'}}

    def add_password(self,website, username, password):
        self.passwords[website] = {'username': username, 'password': password}
        print(f"Password for {website} added successfully!")
    def view_passwords(self):
        if not self.passwords:
            print("No passwords stored yet.")
        else:
            print("Stored passwords:")
            for website, details in self.passwords.items():
                print(f"Website: {website}, Username: {details['username']}, Password: {details['password']}")

    



main_pass=input("Enter the key password: ")
passwords = PasswordManager()

while True:
    if main_pass != "1234":
       print("Incorrect password!")
       exit()
    else:
        print("Welcome to the Password Manager!")    
    
    mode=input("Would you like to add a new password or view existing passwords? (add/view/exit): ").lower()

    if mode == "add":
        
        website = input("Enter the website name: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        passwords.add_password(website, username, password)
    elif mode == "view":
      
        passwords.view_passwords()
    elif mode == "exit":
        print("Exiting the Password Manager. Goodbye!")
        break
    else:
        print("Invalid option. Please choose 'add' or 'view'.")
        continue
    