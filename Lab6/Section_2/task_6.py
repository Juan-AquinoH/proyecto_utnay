class BankAccount:
    bank = "Central Bank"

    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print(f"Client's balance: ${#self.balance}")

    @classmethod
    def show_bank(cls):
        print(f"Bank's name: {cls.bank}")

    @staticmethod
    def convert_currency(value):
        exchange_rate = 20  # Example exchange rate: 1 dollar = 20 pesos
        pesos = value * exchange_rate
        print(f"${value} in dollars is equivalent to ${pesos} in pesos.")
        
# Crear un objeto de BankAccount
account = BankAccount(1000)
# Mostrar el balance del cliente
account.show_balance()
# Mostrar el nombre del banco
BankAccount.show_bank()
# Convertir una cantidad de dólares a pesos
BankAccount.convert_currency(50)

Se coloca el # en print(f"Client's balance: ${#self.balance}") y genera un error de sintaxis:
-2025.14.1-win32-x64\bundled\libs\debugpy\launcher' '62569' '--' 'c:\Users\Lenovo\Desktop\proyecto_utnay\Lab6\Sesction_1\task_3.py'
  File "c:\Users\Lenovo\Desktop\proyecto_utnay\Lab6\Sesction_1\task_3.py", line 18
    @classmethod
    ^
SyntaxError: f-string: expecting a valid expression after '{'