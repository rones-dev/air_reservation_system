from airplane import Airplane

class AirbusA380(Airplane):
    @staticmethod
    def get_name():  # deklarujemy metode get_name
        return "Airbus A380"

    @staticmethod
    def seating_plan():
        return range(1, 41), "ABCDEGHIK"  # tupla zwraca rzedy i siedzenia