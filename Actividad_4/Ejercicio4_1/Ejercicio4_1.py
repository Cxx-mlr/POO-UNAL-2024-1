from SavingsAccount import SavingsAccount

class Ejercicio4_1:
	@staticmethod
	def main():
		print("Cuenta de ahorros")
		
		balance = float(input("Ingrese el saldo inicial: $"))
		annual_interest_rate = float(input("Ingrese la tasa de interés anual: "))
		
		deposit_amount = float(input("Ingrese la cantidad a consignar: $"))
		withdraw_amount = float(input("Ingrese la cantidad a retirar: $"))

		savings_account: SavingsAccount = SavingsAccount(
			balance=balance,
			annual_interest_rate=annual_interest_rate
		)

		savings_account.deposit(deposit_amount)
		savings_account.withdraw(withdraw_amount)

		savings_account.monthly_statement()

		print(f"{savings_account!r}")