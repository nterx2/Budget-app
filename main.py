class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        form = {
            'amount': amount,
            'description' : description
        }
        self.ledger.append(form)

    def withdraw(self, amount, description=""):
        form = {
            'amount' : -amount,
            'description': description
        }
        if self.check_funds(amount):
            self.ledger.append(form)
            return True
        return False
    
    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)
    
    def transfer(self, amount, destination):
        self.withdraw(amount, f"Transfer to {destination.name}")
        destination.doposit(amount, f"Transfer from {self.name}")
        
    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False
        
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
# create object in the ledger instance variable