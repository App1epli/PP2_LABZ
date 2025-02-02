#Create a bank account class that has attributes owner, 
#balance and two methods deposit and withdraw. 
#Withdrawals may not exceed the available balance. 
#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class bankAccount:
    def __init__(self, owner = "", balance = 0):
        self.balance = balance
        self.owner = owner

    def deposit(self):
        aqshaqosu = int(input("Сумма депозита: "))
        self.balance += aqshaqosu
        print("Успешно!")
        print(f"Ваш текущий баланс(тг): {self.balance}")
    
    def withdraww(self):
        withdraw = int(input("Сумма вывода: "))
        if withdraw > self.balance:
            print("Недостаточно средств!")
        else:
            self.balance -= withdraw
            print("Успешно!")
            print(f"Ваш текущий баланс: {self.balance}")

bankOperation = bankAccount(input("ФИО:"), int(input("Введите ваш баланс: ")))
while True:
    typeoper = input("Введите тип операции (Withdraw/Deposit/Exit): ")
    if typeoper == "Withdraw":
        bankOperation.withdraww()
    elif typeoper == "Deposit":
        bankOperation.deposit()
    elif typeoper == "Exit":
        break
    else:
        print("Неправильный ввод операции.")