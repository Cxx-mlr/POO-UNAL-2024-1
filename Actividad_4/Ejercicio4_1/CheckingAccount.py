from __future__ import annotations

from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(
            self,
            balance: float,
            annual_interest_rate: float
    ) -> CheckingAccount:
        super().__init__(balance, annual_interest_rate)
        self._overdraft_amount: float = 0.0

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            self._overdraft_amount += amount - self._balance
            super()._balance = 0.0
        else:
            super().withdraw(amount)
    
    def deposit(self, amount: float) -> None:
        if amount <= self._overdraft_amount:
            self._overdraft_amount -= amount

        else:
            super().deposit(amount - self._overdraft_amount)
            self._overdraft_amount = 0

    def monthly_statement(self) -> None:
        super().monthly_statement()

    def __repr__(self) -> str:
        return (
            f"Saldo: ${self._balance}"
            f"\nComisión mensual = ${self._monthly_fee}"
            f"\nNúmero de transacciones = {self._number_of_deposits + self._number_of_withdrawals}"
            f"\nValor de sobregiro: ${self._overdraft_amount}"
        )