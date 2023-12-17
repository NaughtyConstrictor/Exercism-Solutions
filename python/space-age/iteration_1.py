import re


s = """\
Mercury: orbital period 0.2408467 Earth years
Venus: orbital period 0.61519726 Earth years
Earth: orbital period 1.0 Earth years, 365.25 Earth days, or 31557600 seconds
Mars: orbital period 1.8808158 Earth years
Jupiter: orbital period 11.862615 Earth years
Saturn: orbital period 29.447498 Earth years
Uranus: orbital period 84.016846 Earth years
Neptune: orbital period 164.79132 Earth years\
"""


class SpaceAge:

    ORBITALS = {
        planet.lower(): float(period)
        for planet, period in (
            re.search(
                r"([A-Z][a-z]+): orbital period (\d+\.\d+)", line).groups()
            for line in s.splitlines()
        )
    }

    SECONDS_ON_EARTH = 31557600

    def __init__(self, seconds: int):
        self.seconds = seconds

    def __getattribute__(self, name):
        if name.startswith("on_"):
            return self.calculate_age(name[3:])
        return object.__getattribute__(self, name)

    def calculate_age(self, planet):
        age = self.seconds / (self.SECONDS_ON_EARTH * self.ORBITALS[planet])
        return lambda: round(age, 2)
        