from WorkerInfo import WorkerInfo

class Ejercicio12:
    @staticmethod
    def main():
        worker: WorkerInfo = WorkerInfo.new()
        print(f"\nEl trabajador {worker.name} devengó ${worker.calculate_final_payment():,}")