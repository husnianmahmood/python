from abc import ABC, abstractmethod

class BankAccount(ABC):
  def __init__(self, account_number: int, account_holder: str, balance: float):
    self.account_number: int = account_number
    self.account_holder: str = account_holder
    self._balance: float = balance
  @property
  def balance(self):
    return self._balance
  @balance.setter
  def balance(self, new_balance):
    if new_balance < 0:
      print("Invalid Balance!")
    else:
      self._balance = new_balance

  def deposit(self, deposit_amount:float):
    if deposit_amount <= 0:
      print("Invalid Input!")
    else:
      self._balance += deposit_amount
  def withdraw(self, withdrawal_amount:float):
    if withdrawal_amount <= 0 or withdrawal_amount > self._balance:
      print("Invalid Input!")
    else:
      self._balance -= withdrawal_amount
      print("Amount Withdraw Successfully")
  def calculate_interest(self, interest_rate: float):
    interest = ( self._balance * interest_rate ) / 100
    print(f"Calculated Interest: {interest}")
    return interest
  @abstractmethod
  def account_type(self):
    pass
  @abstractmethod
  def show_details(self):
    pass
class SavingAccount(BankAccount):
  def __init__(self, account_number: int, account_holder: str, balance: float, interest_rate: float ):
    super().__init__(account_number, account_holder, balance)
    self.interest_rate: int = interest_rate

  def account_type(self):
    print("Saving Account")

  def deposit(self, deposit_amount: float):
        super().deposit(deposit_amount)
  def withdraw(self, withdrawal_amount: float):
    super().withdraw(withdrawal_amount)
  def calculate_interest(self, interest_rate: float):
    super().calculate_interest(interest_rate)

  def show_details(self):
    print(f"Account Holder: {self.account_holder}")
    print(f"Account Number: {self.account_number}")
    print(f"Account Balance: {self._balance}")

class CurrentAccount(BankAccount):
  def __init__(self, account_number: int, account_holder: str, balance: float, overdraft_limit: int ):
    super().__init__(account_number, account_holder, balance)
    self.overdraft_limit: int = overdraft_limit

  def account_type(self):
    print("Current Account")
  def withdraw(self, withdrawal_amount: float):

    total_available_funds = self.balance + self.overdraft_limit
    if withdrawal_amount <= 0 or withdrawal_amount > total_available_funds:
      print("Transaction Failed!")
    else:
      self._balance -= withdrawal_amount
      print("Amount Withdrawn Successfully")


  def show_details(self):
    print(f"Account Holder: {self.account_holder}")
    print(f"Account Number: {self.account_number}")
    print(f"Account Balance: {self._balance}")

class FixedDepositAccount(BankAccount):
  def __init__(self, account_number: int, account_holder: str, balance: float, interest_rate: float, maturity_years: int ):
    super().__init__(account_number, account_holder, balance)
    self.interest_rate: float = interest_rate
    self.maturity_years: int = maturity_years
    self.is_matured: bool = False

  def account_type(self):
    print("Fixed Deposit Account")

  def withdraw(self, withdrawal_amount: float):
    if not self.is_matured:
      print("Withdrawal Not Allowed Before Maturity")
    else:
      super().withdraw(withdrawal_amount)

  def calculate_interest(self):
    interest = self.balance * self.interest_rate * self.maturity_years
    print(f"Calculated Fixed Deposit Interest: {interest}")
    return interest

  def show_details(self):
    print(f"Account Holder: {self.account_holder}")
    print(f"Account Number: {self.account_number}")
    print(f"Account Balance: {self._balance}")
    print(f"Interest Rate: {self.interest_rate}%")
    print(f"Maturity Period: {self.maturity_years} Years")
    print(f"Matured Status: {self.is_matured}")


#objects
saving1 = SavingAccount(11, "Ali", 50.00, 2.4)
saving2 = SavingAccount(12, "Ahmad", 60.00, 2.6)

current1 = CurrentAccount(13, "Usman", 70.00, 100.00)
fixed1 = FixedDepositAccount(14, "Hamza", 80.00, 3.1, 2)


saving1.show_details()
saving1.deposit(10)
saving1.withdraw(10)
saving1.calculate_interest(10)
saving1.account_type()
print()
saving2.show_details()
saving2.deposit(20)
saving2.withdraw(20)
saving2.calculate_interest(20)
saving2.account_type()
print()
current1.show_details()
current1.deposit(30)
current1.withdraw(30)
current1.calculate_interest(30)
current1.account_type()
print()
fixed1.show_details()
fixed1.deposit(40)
fixed1.withdraw(40)
fixed1.calculate_interest()
fixed1.account_type()
for i in range(5):
  print()
accounts = [
    saving1,
    saving2,
    current1,
    fixed1
]
for account in accounts:
    account.account_type()
    account.show_details()

saving1.balance = -100
print(f"Current Balance remains: {saving1.balance}")
