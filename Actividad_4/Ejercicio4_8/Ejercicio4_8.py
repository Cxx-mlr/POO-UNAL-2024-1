from CyclingRace.Team import Team
from CyclingRace.Sprinter import Sprinter
from CyclingRace.Climber import Climber
from CyclingRace.TimeTrialist import TimeTrialist

class Ejercicio4_8:
	@staticmethod
	def main():
		team = Team(
			name="Sky",
			country="Estados Unidos"
		)

		sprinter = Sprinter(
			identifier=123979,
			name="Geraint Thomas",
			average_power=320.0,
			average_speed=25.0
		)

		climber = Climber(
			identifier=123980,
			name="Egan Bernal",
			average_acceleration=25.0,
			ramp_grade=10.0
		)

		time_trialist = TimeTrialist(
			identifier=123981,
			name="Jonathan Castroviejo",
			maximum_speed=120.0
		)

		team.add_cyclist(sprinter)
		team.add_cyclist(climber)
		team.add_cyclist(time_trialist)

		sprinter._Cyclist__set_accumulated_time(365.0)
		climber._Cyclist__set_accumulated_time(385.0)
		time_trialist._Cyclist__set_accumulated_time(370.0)

		team.calculate_total_time()

		print(team, end="\n\n")
		team.list_cyclists()