# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции - функции. Дополнительно сохраняйте все операции
# поступления и снятия средств в список.

balance = 0
transactions = []


def deposit(amount):
    global balance
    global transactions
    if balance >= 5000000:
        tax = balance * 0.1
        balance -= tax
        transactions.append(("Налог на богатство -", tax))
    if amount % 50 != 0:
        print("Сумма должна быть кратна 50")
        return
    balance += amount
    transactions.append(("Пополнение", amount))
    if len(transactions) % 3 == 0:
        transactions.append(("Проценты +", balance*0.03))
        balance = balance * 1.03     
    print(f"Баланс: {balance}")


def withdraw(amount):
    global balance
    global transactions
    if amount % 50 != 0:
        print("Сумма должна быть кратна 50")
        return
    if amount > balance:
        print("Недостаточно средств на счете")
        return
    if balance >= 5000000:
        tax = balance * 0.1
        balance -= tax
        transactions.append(("Налог на богатство -", tax))
    balance -= amount + min(max(amount * 0.015, 30), 600)
    transactions.append(("Снятие", amount))
    if len(transactions) % 3 == 0:
        interest = balance * 0.03
        balance += interest
        transactions.append(("Проценты", interest))
    print(f"Баланс: {balance}")

def print_balance():
    global balance
    print(f"Баланс: {balance}")

def print_transactions():
    global transactions
    for transaction in transactions:
        print(f"{transaction[0]}: {transaction[1]}")


def run_device():
    while True:
        print("Выберите действие:\n1 - пополнить\n2 - снять\n3 - баланс\n4 - вывести список транзакций\n5 - выйти")
        action = input().lower()
        if action == "1":
            print("Введите сумму для пополнения") 
            deposit(int(input()))
        elif action == "2":
            print("Введите сумму для снятия")
            withdraw(int(input()))
        elif action == "4":
            print_transactions()
        elif action == "3":
            print_balance()
        elif action == "5": 
            break
        else:
            print("Команда не распознана")


run_device()