class PasswordManager:
    def add_password(self,website, username, password):
        with open("passwords.txt", "a") as f:
         f.write(f"Website: {website}, Username: {username}, Password: {password}\n")
    def view_passwords(self):
        with open("passwords.txt", "r") as f:
            passwords = f.readlines()
            if not passwords:
                print("No passwords stored.")
            else:
                print("Stored Passwords:")
                for password in passwords:
                    print(password.strip())
    



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
    