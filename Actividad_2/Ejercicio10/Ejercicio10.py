from Student import Student

class Ejercicio10:
    @staticmethod
    def main():
        student: Student = Student.new()
        print(f"El Estudiante con número de inscripción {student.registration_number} y nombre {student.name} debe pagar ${student.calculate_tuition_feed():,}")