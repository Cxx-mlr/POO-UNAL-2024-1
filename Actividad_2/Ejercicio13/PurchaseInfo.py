from __future__ import annotations

class PurchaseInfo:
    purchase_amount: float
    ball_color: str

    def __init__(self, purchase_amount: float, ball_color: str) -> PurchaseInfo:
        self.purchase_amount = purchase_amount
        self.ball_color = ball_color

    @classmethod
    def new(cls) -> PurchaseInfo:
        print("Ingrese los datos de la compra")
        purchase_amount = float(input("\tPrecio: "))
        ball_color = input("\tColor de la bolita: ")

        return cls(purchase_amount=purchase_amount, ball_color=ball_color.lower())

    def calculate_discount_percentage(self) -> float:
        match self.ball_color:
            case "blanca":
                return 0
            case "verde":
                return 10
            case "amarilla":
                return 25
            case "azul":
                return 50
            case "roja":
                return 100
            case color:
                raise RuntimeError(f'Invalid ball color. Only "blanca", "verde", "amarilla", "azul", and "roja" are allowed.')

    def calculate_final_payment(self) -> float:
        return (100 - self.calculate_discount_percentage())/100 * self.purchase_amount

    def __str__(self) -> str:
        return (f"\tValor de la compra: ${self.purchase_amount:,}" +
                f"\n\tColor de la bolita: {self.ball_color.capitalize()}" +
                f"\n\tPorcentaje de descuento: {self.calculate_discount_percentage()}%" +
                f"\n\tTotal a pagar: ${self.calculate_final_payment():,}")