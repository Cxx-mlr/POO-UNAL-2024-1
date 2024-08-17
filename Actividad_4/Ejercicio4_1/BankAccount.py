from __future__ import annotations

class BankAccount:
    def __init__(
            self,
            balance: float,
            annual_interest_rate: float
    ) -> BankAccount:
        self._balance: float = balance
        self._annual_interest_rate: float = annual_interest_rate

        self._number_of_deposits: int = 0
        self._number_of_withdrawals: int = 0
        self._monthly_fee: float = 0.0

    def deposit(self, amount: float) -> None:
        self._balance += amount
        self._number_of_deposits += 1

    def withdraw(self, amount: float) -> None:
        if amount  > self._balance:
            print("La cantidad a retirar excede el saldo actual")
        else:
            self._balance -= amount
            self._number_of_withdrawals += 1

    def calculate_monthly_interest(self) -> None:
        monthly_interest_rate = self._annual_interest_rate / 12
        monthly_interest = monthly_interest_rate * self._balance

        self._balance += monthly_interest

    def monthly_statement(self) -> None:
        self._balance -= self._monthly_fee
        self.calculate_monthly_interest()