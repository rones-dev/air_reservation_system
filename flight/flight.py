class Flight:
    def __init__(self, flight_number, plane):
        self.flight_number = flight_number  # obiekt klasy Filight
        self.plane = plane  # obiekt klasy Filight

        rows, letters = self.plane.seating_plan()  # dwie zmienne gdzie rozpakowywujemy
        self.seats = [None] + [{letter: None for letter in letters} for _ in rows]  # _ dummy name

    def get_airline(self):
        return self.flight_number[:2]       # metoda zwraca numer lotu po slicingu

    def get_number(self):  # deklarujemy metode ktora zwraca slicing pola flight number
        return self.flight_number[2:]

    def get_airplane_model(self):
        return self.plane.get_name()  # zwracamy wynik działania metody get_name

    def _parse_seat(self, seat="12C"):  # _ kod tylko dla tej kalsy - private
        rows, letters = self.plane.seating_plan()  # tworzymy 2 zmienne rows i letters gdzie wynik dzialania rozpakowaujemy

        letter = seat[-1]  # slicing

        if letter not in letters:
            raise ValueError(f"Invalid seat letter {letter}")

        row_text = seat[:-1]
        try:
            row = int(row_text)  # tworzymy  zmienna row jako intiger
        except ValueError:
            raise ValueError(f"Invalid seat number {row_text}")

        if row not in rows:
            raise ValueError(f"Row {row} is out of range")

        return row, letter  # pakujemy tuple

    def allocate_passenger(self, passenger="Jan K.", seat="12C"):  # parametry defaultowe
        row, letter = self._parse_seat(seat)

        if self.seats[row][letter] is not None:  # self.seat lista
            raise ValueError(f"Seat {seat} is already occupied.")

        self.seats[row][letter] = passenger  #

    def relocate_passengers(self, seat_from, seat_to):
        row_from, letter_from = self._parse_seat(seat_from)

        if self.seats[row_from][letter_from] is None:  # slacing na liscie slowników
            raise ValueError(f"No passenger on the {seat_from} seat.")

        row_to, letter_to = self._parse_seat(seat_to)

        if self.seats[row_to][letter_to] is not None:
            raise ValueError(f"Seat {seat_to} is already occupied.")

        self.seats[row_to][letter_to] = self.seats[row_from][letter_from]
        self.seats[row_from][letter_from] = None

    def get_empty_seats(self):
        return sum(sum(1 for seat in row.values() if seat is None)  # comprehension
                   for row in self.seats   # comprehension
                   if row is not None)

    def print_cards(self, printer):     # printer - tu deklaracja funkcji
        passengers = self.get_passengers()

        for passenger, seat in passengers: # rozpakowanie tupli
            printer(passenger, seat, self.get_airplane_model(), self.flight_number) # wywolanie print z parametrami - 4 stringi

    def get_passengers(self):
        passengers = []  # tworzymy zmienna pusta liste
        rows, letters = self.plane.seating_plan()

        for row in rows:
            for letter in letters:
                passenger = self.seats[row][letter] # tworzymy zmienna passenger
                if passenger is not None:
                    passenger_data = passenger, f"{row}{letter}"     # pakujemy tuple
                    passengers.append(passenger_data)

        return passengers  # listat tupli dwu elementowych