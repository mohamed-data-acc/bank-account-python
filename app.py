from datetime import datetime

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount
        now = datetime.now()
        print(f"تم ايداع {amount} جنية - {now.strftime('%A %d %B %Y - %I:%M %p')}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("الرصيد غير كافي")
        else:
            self.__balance -= amount
            now = datetime.now()
            print(f"تم سحب {amount} جنية - {now.strftime('%A %d %B %Y - %I:%M %p')}")

    def get_balance(self):
        return self.__balance
class SavingsAccount(BankAccount):
    def deposit(self, amount):
        Bouns=amount*0.05
        Total=Bouns+amount
        super().deposit(Total)
        print(f"مبروك! اتضافت فائدة {Bouns} جنية")
    def withdraw(self, amount):
        fees=amount*0.02
        total=amount+fees
        super().withdraw(total)
        print(f"تم خصم رسوم {fees} جنية")

print('========حساب عادي=========')
acc = BankAccount()
acc.deposit(8000)
acc.withdraw(522)
print(f"الرصيد الحالي: {acc.get_balance()} جنية")
print("======حساب توفير======")
sav=SavingsAccount()
sav.deposit(9000)
sav.withdraw(800)
print(f"الرصيد الحالي: {sav.get_balance()} جنية")












