
class BankAccount(object):
	def withdraw(self):
		pass

	def deposit(self):
		pass
		
class SavingsAccount(BankAccount):
	def __init__(self):
		self.balance = 500
		
	def deposit(self, amount):
		self.amount = amount
		
		if (amount < 0):
			return "Invalid deposit amount"
		else:
			self.balance += amount
		return self.balance

	def withdraw(self, amount):
		self.amount = amount
		
		if (amount < 0):
			return "Invalid withdraw amount"
		elif (amount == 0):
			return self.balance
		elif (amount > 0):
			if (amount <= self.balance):
				if ((self.balance-amount) >= 500):
					self.balance -= amount
				else:
					return "Cannot withdraw beyond the minimum account balance"
			elif (amount > self.balance):
				return "Cannot withdraw beyond the current account balance"
			else:
				pass
		else:
			pass
		
		return self.balance
				
				
class CurrentAccount(BankAccount):
	def __init__(self):
		self.balance = 0

	def deposit(self, amount):
		self.amount = amount
		
		if (amount < 0):
			return "Invalid deposit amount"
		elif (amount >= 0):
			self.balance += amount
		else:
			pass
		return self.balance

	def withdraw(self, amount):
		self.amount = amount

		if (amount < 0):
			return "Invalid withdraw amount"
		elif (amount == 0):
			return self.balance
		elif (amount > 0):
			if (amount <= self.balance):
				self.balance -= amount
			else:
				return "Cannot withdraw beyond the current account balance"
		else:
			pass

		return self.balance