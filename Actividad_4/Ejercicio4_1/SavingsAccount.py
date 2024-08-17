from __future__ import annotations

from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(
            self,
            balance: float,
            annual_interest_rate: float
    ) -> SavingsAccount:
        super().__init__(balance, annual_interest_rate)

    def deposit(self, amount: float) -> None:
        if self._is_active:
            super().deposit(amount)

    def withdraw(self, amount: float) -> None:
        if self._is_active:
            super().withdraw(amount)

    def monthly_statement(self) -> None:
        if (number_of_withdrawals := self._number_of_withdrawals) > 4:
            super()._monthly_fee += (number_of_withdrawals - 4.0) * 1_000.0

        super().monthly_statement()

    @property
    def _is_active(self) -> bool:
        return self._balance >= 10_000.0
    
    def __repr__(self) -> str:
        return (
            f"Saldo: ${self._balance:,}"
            f"\nComisión mensual: ${self._monthly_fee:,}"
            f"\nNúmero de transacciones: {self._number_of_deposits + self._number_of_withdrawals}"
        )