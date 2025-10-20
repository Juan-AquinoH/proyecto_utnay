#Create a class named BankAccount with the following characteristics: 
#o A class attribute named bank = "Central Bank". 
#o An instance method named show_balance() that prints the client’s balance. 
#o A class method named show_bank() that prints the bank’s name. 
#o A static method named convert_currency(value) that receives an amount in 
#dollars and converts it to pesos (use a fixed exchange rate of your choice). 
#Create an object of the BankAccount class and show the results of the three types of 
#methods.
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


# Resultados

#Client's balance: $1000
#Bank's name: Central Bank
#$50 in dollars is equivalent to $1000 in pesos.