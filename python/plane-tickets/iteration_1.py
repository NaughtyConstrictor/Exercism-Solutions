"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    SEATS = "ABCD"
    NUM_SEATS = len(SEATS)
    for i in range(number):
        yield SEATS[i % NUM_SEATS]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    SEATS = "ABCD"
    NUM_SEATS = len(SEATS)
    row_num = 0
    BAD_NUMBER = 13
    for i in range(number):
        seat_num = i % NUM_SEATS
        if seat_num == 0:
            row_num += 1
            if row_num == BAD_NUMBER:
                row_num += 1
                
        yield f"{row_num}{SEATS[seat_num]}"


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    return {
        passenger: seat_num
        for passenger, seat_num in zip(passengers, generate_seats(len(passengers)))
    }

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    TICKET_LENGTH = 12
    FILL_CHAR = "0"
    for seat_num in seat_numbers:
        yield (seat_num + flight_id).ljust(TICKET_LENGTH, FILL_CHAR)
        