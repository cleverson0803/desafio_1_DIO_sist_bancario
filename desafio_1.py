class BankingSystem:
    def __init__(self):
        """Initialize the banking system with zero balance and empty lists of deposits and withdrawals."""
        self.balance = 0
        self.deposits = []  # List to store deposits
        self.withdrawals = []  # List to store withdrawals

    def deposit(self, amount):
        """Make a deposit into the account."""
        if amount > 0:
            # Add the amount to the balance and record the deposit in the list of deposits
            self.deposits.append(amount)
            self.balance += amount
            print(f'\nDeposit of ${amount:.2f} successful.')
        else:
            print('\nThe deposit amount must be positive.')

    def withdraw(self, amount):
        """Make a withdrawal from the account."""
        if len(self.withdrawals) >= 3:
            print('\nMaximum daily withdrawal limit reached.')
            return
        if amount <= 0:
            print('\nThe withdrawal amount must be positive.')
            return
        if amount > 500:
            print('\nMaximum withdrawal limit is $500.00 per transaction.')
            return
        if self.balance < amount:
            print('\nInsufficient balance to make the withdrawal.')
            return
        # Deduct the amount from the balance and record the withdrawal in the list of withdrawals
        self.withdrawals.append(amount)
        self.balance -= amount
        print(f'\nWithdrawal of ${amount:.2f} successful.')

    def statement(self):
        """Display the account statement, listing deposits, withdrawals, and current balance."""
        if not self.deposits and not self.withdrawals:
            print('\nNo transactions have been made.')
            return
        print('\nStatement:')
        print('-' * 30)
        print('{:<12} {:<10}'.format('Transaction', 'Amount'))
        print('-' * 30)
        # List deposits
        for deposit in self.deposits:
            print('{:<12} {:<10.2f}'.format('Deposit:', deposit))
        # List withdrawals
        for withdrawal in self.withdrawals:
            print('{:<12} {:<10.2f}'.format('Withdrawal:', withdrawal))
        print('-' * 30)
        # Display current balance
        print('{:<12} {:<10.2f}'.format('Current Balance:', self.balance))


# Function to display the menu options
def display_menu():
    print("\nOptions:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Statement")
    print("0. Exit")


# Example usage of the banking system
bank = BankingSystem()

while True:
    display_menu()
    option = input("\nChoose an option: ")

    if option == "1":
        amount = float(input("\nEnter the amount to deposit: "))
        bank.deposit(amount)
    elif option == "2":
        amount = float(input("\nEnter the amount to withdraw: "))
        bank.withdraw(amount)
    elif option == "3":
        bank.statement()
    elif option == "0":
        print("\nExiting...")
        break
    else:
        print("\nInvalid option. Please choose a valid option.")
