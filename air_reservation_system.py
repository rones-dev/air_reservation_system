# from pprint import pprint
from flight import Flight
# from airplane import Airplane
from planes import *
from helpers import *


def make_flight():

    # ctrl + shift + strzała
    boeing = Boeing777()  # deklarujemy zmienna bieing - przypisujemy obiekt klasy boeing
    # print(boeing.num_seats())
    airbus = AirbusA380()
    # print(airbus.num_seats())
    # print(boeing.get_name())

    f = Flight("L0127", boeing)  # obiekt klasy filight

    f.allocate_passenger("Jasrosław L.", "12A")  # na obiekcie f wywolujemy metode all..., przekazujemy parametry
    f.allocate_passenger("Lech K.", "12B")
    f.allocate_passenger("Zbigniew Z.", "12C")
    f.allocate_passenger("Katarzyna F.", "21C")

    f.relocate_passengers("12B", "2C")
    f.relocate_passengers("12A", "2B")
    # print(f.flight_number)
    # print(f.get_airline())
    # print(f.get_number())
    # print(f.get_airplane_model())
    # pprint(f.seats)               # pobieramy pole seats obiektu f
    # print(f.get_empty_seats())

    # card_printer("Jan Seaba Bach", "13B", "Airbus A3808", "BA234")
    # card_printer("Antonio Materac", "14C", "Airbus A3808", "BA247")
    f.print_cards(card_printer)


make_flight()