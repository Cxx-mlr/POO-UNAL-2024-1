from CyclingRace.Team import Team
from CyclingRace.Sprinter import Sprinter
from CyclingRace.Climber import Climber
from CyclingRace.TimeTrialist import TimeTrialist

class Ejercicio4_8:
	@staticmethod
	def main():
		team = Team("Sky", "Estados Unidos")
		sprinter = Sprinter(123979, "Geraint Thomas", 320.0, 25.0)
		climber = Climber(123980, "Egan Bernal", 25.0, 10.0)
		time_trialist = TimeTrialist(123981, "Jonathan Castroviejo", 120.0)

		team.add_cyclist(sprinter)
		team.add_cyclist(climber)
		team.add_cyclist(time_trialist)

		sprinter._Cyclist__set_accumulated_time(365.0)
		climber._Cyclist__set_accumulated_time(385.0)
		time_trialist._Cyclist__set_accumulated_time(370.0)

		team.calculate_total_time()

		print(team, end="\n\n")
		team.list_cyclists()