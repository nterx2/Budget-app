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
        self.ledger.append(form)
    
    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)
        
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
# create object in the ledger instance variable