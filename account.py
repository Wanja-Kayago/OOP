class Account:
  def __init__(self, owner_name, opening_balance,pin,number):
    self.owner_name = owner_name
    self.balance = opening_balance
    self.__pin = pin
    self.__balance = 0
    self.number = number
    self.transactions = []
    self.overdraft_limit = 0
    self.minimum_balance = 0
    self.is_frozen = False

  # Shows the balance in the account
  def show_balance(self,pin):
        if pin == self.__pin:
            return self.__balance
        else:
            return "wrong pin"
        
  # View Account Details
  def view_details(self):
    print(f"Account Owner: {self.owner_name}")
    print(f"Balance: ${self.__balance}")

  # Change Account Owner
  def change_owner(self, new_owner_name):
    self.owner_name = new_owner_name

  # Account Statement (last 3 transactions)
  def generate_statement(self):
    print("Recent Transactions:")
    for transaction in self.transactions[-3:]:
      print(transaction)

  # Set Overdraft Limit
  def set_overdraft_limit(self, limit):
    self.overdraft_limit = limit

  # Interest Calculation 
  def calculate_interest(self):
    pass

  # Freeze/Unfreeze Account
  def freeze_account(self):
    self.is_frozen = True
    print("Account Frozen")

  def unfreeze_account(self):
    self.is_frozen = False
    print("Account Unfrozen")

  # Transaction History
  def get_transaction_history(self):
    print("Transaction History:")
    for transaction in self.transactions:
      print(transaction)

  # Set Minimum Balance
  def set_minimum_balance(self, minimum):
    self.minimum_balance = minimum

  # Transfer Funds 
  def transfer_funds(self, destination_account, amount):
    if self.balance + self.overdraft_limit >= amount and not self.is_frozen:
      self.balance -= amount
      destination_account.balance += amount
      self.add_transaction(f"Transferred ${amount:.2f} to {destination_account.owner_name}")
      destination_account.add_transaction(f"Received ${amount:.2f} from {self.owner_name}")
      print(f"Transfer of ${amount:.2f} successful")
    else:
      print("Transfer failed")

  # Close Account 
  def close_account(self):
    print(f"Account for {self.owner_name} closed")

  # add transactions to the history
  def add_transaction(self, description):
    self.transactions.append(description)
