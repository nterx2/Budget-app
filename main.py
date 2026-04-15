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
        output += f"Total: {self.get_balance():.2f}"
        return output

def calculate_spent_pencentage(categories):
    withdrawal = []
    for category in categories:
        total_withdraw = sum(abs(item['amount']) for item in category.ledger if item['amount'] < 0 )
        withdrawal.append(total_withdraw)
    total_spend = sum(withdrawal)
    if total_spend == 0:
        return [0] * len(categories)
    percentages = [(withdraw / total_spend * 100) // 10 * 10 for withdraw in withdrawal]
    return percentages

def create_spend_chart(categories):
    percentage = calculate_spent_pencentage(category)
    names = [cat.name for cat in category]
    max_len = max(len(name) for name in names) # use max_len for set round in loop
    result = "Percentage spent by category\n"
    for y in range(100, -1, -10):
        result += f"{y :>3}| "
        for p in percentage:
            if p >= y:
                result += "o  "
            else:
                result += "   "
        result += "\n"
    result += "    " + "-" * (len(percentage)* 3 + 1) + "\n"

    for x in range(max_len):
        row = "     " # space in front of line (5 space)
        for name in names:
            if x < len(name):
                row += f"{name[x]}  " # print character follow sequence
            else:
                row += "   " # if x index greater than len(name) add 3 space(1 character + 2 space)
        if x < max_len - 1:
            result += row + "\n"
        else:
            result += row
    return result

# create object in the ledger instance variable
food = Category('Food')
clothing = Category('Clothing')
auto = Category('Auto')
# calling method of class
food.deposit(1000, 'deposit')
food.withdraw(274.2, 'meat cereal chocolate, milk, washing powder, wine')
food.withdraw(91.4, 'restaurant')
food.withdraw(45.7, 'snack, Cola')
clothing.deposit(500 , 'deposit')
clothing.withdraw(52.34, 'T-shirt')
clothing.transfer(75, food)
auto.deposit(200, 'deposit')
auto.withdraw(85, 'fuel')
category = [food, clothing, auto]

print(food)
print(create_spend_chart(category))
