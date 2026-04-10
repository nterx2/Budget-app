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
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination.name}")
            destination.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
        
    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False
    
    def __str__(self):
        output = f"{self.name:*^30}\n"
        for item in self.ledger:
            output += f"{item['description']:<23.23}{item['amount']:>7.2f}\n"
        output += f"Total: {self.get_balance()}"
        return output
        
food = Category('Food')
# create object in the ledger instance variable
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)