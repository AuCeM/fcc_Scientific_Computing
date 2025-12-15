class Category:
    def __init__(self, cat):
        self.category = cat
        self.ledger = []
        self.balance = 0

    def deposit(self, d_amount, desc=''):
        self.ledger.append({'amount': d_amount, 'description': desc})
        self.get_balance(d_amount)

    def withdraw(self, w_amount, desc=''):
        if self.check_funds(w_amount):
            w_amount *= float(-1)
            self.ledger.append({'amount': w_amount, 'description': desc})
            self.get_balance(w_amount)
            return True
        else:
            return False

    def transfer(self, t_amount, other_category):
        if not self.check_funds(t_amount):
            return False
        else:
            transfer_to = f'Transfer to {other_category.category}'
            self.withdraw(t_amount, transfer_to)
            transfer_from = f'Transfer from {self.category}'
            other_category.deposit(t_amount, transfer_from)
            return True

    def get_balance(self, quantity):
        self.balance += quantity
        return self.balance

    def check_funds(self, quantity):
        if quantity > self.balance:
            return False
        else:
            return True

    def __str__(self):
        receipt = self.category.center(30, '*') + '\n'
        for row in range(0, len(self.ledger)):
            _desc_ledger = self.ledger[row]['description']
            _amount_ledger = self.ledger[row]['amount']
            receipt += (_desc_ledger[:23] + ' ' * (30 - len(_desc_ledger[:23]) - len(f"{_amount_ledger:.2f}"))
                        + f"{_amount_ledger:.2f}") + '\n'
        receipt += f'Total: {self.balance:.2f}'
        return receipt


def create_spend_chart(budget_list):
    import math as mt

    cat_list = [x.category for x in budget_list]
    budget_len = len(budget_list)  # category list length
    bar_nums = list(range(100, -1, -10))
    gasto_por_categoria = []

    # gets total withdrawn amount, category withdrawals and calculates percentages...respectively
    for m in budget_list:
        cantidad_por_cat = 0
        for n in m.ledger:
            if n['amount'] < 0:
                cantidad_por_cat += abs(n['amount'])
        gasto_por_categoria.append(cantidad_por_cat)

    cantidad_total = 0
    for y in category_list:
        for z in y.ledger:
            if z['amount'] < 0:
                cantidad_total += abs(z['amount'])

    cat_percent = [mt.floor((_ / cantidad_total) * 100 // 10) * 10 for _ in gasto_por_categoria]

# creates new lists: the order of the list holds the order of each character of the previous list.
# i.e. first list element holds the first letter of each word in category list,
# second list element holds second letter of each word in category list, etc...
    rearranged_words = []
    nested_list = cat_list.copy()
    longest_word = max(cat_list, key=len)

    for i in range(len(cat_list)):
        nested_list[i] = " ".join(cat_list[i])
        nested_list[i] = nested_list[i].split(" ")

    r_num = len(longest_word)
    for row in range(r_num):
        rearranged_words.append([])
        for col in range(budget_len):
            if row < len(nested_list[col]):
                if col == 0:
                    rearranged_words[row].append(f'{nested_list[col][row]:>6}')
                else:
                    if len(rearranged_words[row]) > 0:
                        rearranged_words[row].append(f'{nested_list[col][row]:>2}')
                    else:
                        rearranged_words[row].append(f'{nested_list[col][row]:>{3 * (col + 2)}}')
            else:
                continue

# attaches 'o' character to each of the top rows to create the bar chart and after row 13 joins rearranged_words list
    circle = 'o'
    matrix = []
    row_num = 12 + len(max(cat_list, key=len))
    col_num = 4 + 3 * budget_len + 1
    bars = f'Percentage spent by category\n'

    for r in range(row_num):
        matrix.append([])

        if r < len(bar_nums):
            matrix[r] = f'{bar_nums[r]:>3}|'
            for c in range(col_num):
                for i in range(budget_len):
                    if cat_percent[i] >= bar_nums[r] and (c - (2 * i + 5) == i):
                        if c == 5:
                            matrix[r] += f'{circle:>2}'
                        elif c > 5 and c % 3 == 2:
                            matrix[r] += f'{circle:>3}'
        elif r == 11:
            matrix[r] = " " * 4 + "---" * budget_len + "-"

    for fila in range(12, 12 + r_num):
        matrix[fila] = ' '.join(rearranged_words[fila - 12])

    for k in range(len(matrix)):
        while len(matrix[k]) < col_num:
            matrix[k] += " "

    for _ in range(len(matrix)):
        if _ == len(matrix) - 1:
            bars += f'{matrix[_]}'
        else:
            bars += f'{matrix[_]}' + '\n'
    return bars


food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
clothing.deposit(600)
clothing.withdraw(24.48, 'jeans')
business = Category('Business')
entertainment = Category('Entertainment')
business.deposit(500)
business.withdraw(16.40, 'packages')
entertainment.deposit(300)
entertainment.withdraw(12.61, 'games')

category_list = [food, clothing, business, entertainment]
print(create_spend_chart(category_list))
