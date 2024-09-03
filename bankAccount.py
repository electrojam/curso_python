class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}.  Tu saldo actual es {self.balance}")
        else:
            print("No se puede hacer el depósito.  Cuenta inactiva.")

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}.  Tu saldo actual es {self.balance}")
            else:
                print("No se puede hacer el retiro.  Fondos insuficientes en la cuenta")
        else:
            print("No se puede hacer el retiro.  Cuenta inactiva")
    
    def deactivate_account(self):
        self.is_active = False
        print("La cuenta ha sido desactivada")

    def activate_account(self):
        self.is_active = True
        print("La cuenta ha sido activada")

account1 = BankAccount("Piter", 1000)
account2 = BankAccount("Wendy", 1500)

account1.deposit(200)
account2.deposit(500)
account1.deactivate_account()
account1.deposit(50)
account1.activate_account()
account1.deposit(50)


