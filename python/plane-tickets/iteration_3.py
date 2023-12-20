"""Functions to automate Conda airlines ticketing system."""


from collections.abc import Generator
from itertools import count, cycle, islice
from typing import Literal, TypeAlias


SEATS = "ABCD"
SEATS_PER_ROW = len(SEATS)
BAD_NUMBER = 13
TICKET_LENGTH = 12
FILL_CHAR = "0"


SeatLetter: TypeAlias = Literal[list(SEATS)]


def generate_seat_letters(number: int) -> Generator[SeatLetter, None, None]:
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    yield from islice(cycle(SEATS), 0, number)


def generate_seats(number: int) -> Generator[str, None, None]:
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    yield from map(
        lambda seat_num, seat, _: f"{seat_num // SEATS_PER_ROW}{seat}",
        filter(
            lambda seat_num: seat_num // SEATS_PER_ROW != BAD_NUMBER,
            count(SEATS_PER_ROW)
        ),
        cycle(SEATS),
        range(number)
    )
    

def assign_seats(passengers: list[str]) -> dict[str, str]:
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    return dict(zip(passengers, generate_seats(len(passengers))))


def generate_codes(
    seat_numbers: list[str], flight_id: str
    ) -> Generator[str, None, None]:
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    return  (
        (seat_num + flight_id).ljust(TICKET_LENGTH, FILL_CHAR)
        for seat_num in seat_numbers
    )
    