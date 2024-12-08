# MINI-BANK-APPLICATION
MINI BANK APPLICATION BY USING PYTHON SCRIPTING LANGUAGE WITH PIN ENTRY FEATURE.

A Mini Bank Application written in Python with a PIN entry feature is a simple program that simulates basic banking functionalities such as checking balances, depositing funds, and withdrawing money, all while ensuring user security with PIN verification. Here's a breakdown of how such an application can be structured:

**1. Application Overview**

**User Login:** The user enters a PIN to authenticate themselves.
Basic Bank Operations: Once logged in, users can:
Check their account balance.
Deposit money into their account.
Withdraw money from their account.
**PIN Protection:** The application uses a PIN for secure login to ensure that only authorized users can access their bank accounts.
Data Storage: For simplicity, account details (such as balance) can be stored in variables or a text file (in a real-world application, a database would be used).

**2. Features**
**PIN Entry:** The application asks the user to enter their PIN at the start. If the entered PIN matches the pre-set value, access is granted; otherwise, access is denied.
**Account Balance:** A feature that displays the current account balance.
**Deposit Funds:** The user can deposit a specified amount of money into their account.
**Withdraw Funds:** The user can withdraw a specified amount of money if their balance is sufficient.
**Exit Option:** Allows the user to exit the application gracefully.

**3. Implementation in Python**
Below is a sample implementation of a Mini Bank Application using Python with a PIN entry feature:
############################################################################################################################################################################################################

class MiniBank:
    def __init__(self, pin, balance=0.0):
        self.pin = pin      # Initialize the user's PIN
        self.balance = balance  # Initialize the account balance
    
    def authenticate(self, entered_pin):
        """Method to authenticate the user with PIN"""
        if entered_pin == self.pin:
            print("PIN correct. Access granted.")
            return True
        else:
            print("Incorrect PIN. Access denied.")
            return False
    
    def check_balance(self):
        """Method to display account balance"""
        print(f"Your current balance is: ${self.balance}")
    
    def deposit(self, amount):
        """Method to deposit money into the account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Your new balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """Method to withdraw money from the account"""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. Your new balance is ${self.balance}.")
            else:
                print("Insufficient balance for withdrawal.")
        else:
            print("Withdrawal amount must be positive.")
    
    def main_menu(self):
        """Display the main menu to the user"""
        while True:
            print("\n--- Mini Bank ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            
            choice = input("Please choose an option (1-4): ")
            
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(amount)
            elif choice == '4':
                print("Thank you for using Mini Bank. Goodbye!")
                break
            else:
                print("Invalid option. Please choose between 1-4.")

# Create a MiniBank instance with a preset PIN (e.g., 1234)
bank_account = MiniBank(pin="1234")

# Start the application by asking the user to enter PIN
entered_pin = input("Enter your PIN to access your account: ")

if bank_account.authenticate(entered_pin):
    # If authentication is successful, display the main menu
    bank_account.main_menu()
else:
    print("Access denied. Please try again with the correct PIN.")

############################################################################################################################################################################################################

**4. Explanation of the Code:**
MiniBank Class: This class contains methods for:

PIN authentication (authenticate method) to check if the user has entered the correct PIN.
Checking balance (check_balance method).
Depositing money (deposit method).
Withdrawing money (withdraw method).
Displaying the main menu (main_menu method) to let the user interact with the application.
Authentication: When the program starts, the user is prompted to enter a PIN. If the PIN is correct, the main menu with options to check balance, deposit, withdraw, or exit is displayed. If the PIN is incorrect, access is denied.

Deposit and Withdrawal: Users can deposit or withdraw money as long as they have sufficient balance. The program checks if the balance is enough for withdrawal and prevents overdraft.

Error Handling: The application ensures that only positive values can be deposited or withdrawn and prevents invalid options.

**5. Possible Extensions:**
Multiple User Support: The app could be extended to support multiple users with different PINs and balances.
Data Persistence: Instead of keeping the balance in memory, it could be saved to a file or database, so even after the application is closed, the user’s data is preserved.
Password Encryption: For a more secure implementation, the PIN could be encrypted using hashing techniques to prevent unauthorized access in case of file exposure.
**6. Security Considerations:**
The application’s PIN system is a basic security feature but could be enhanced using more advanced methods such as two-factor authentication or encrypted passwords for a real-world application.


