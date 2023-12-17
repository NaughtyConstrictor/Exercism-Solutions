import functools


HEADER = ["Team                           | MP |  W |  D |  L |  P"]


@functools.total_ordering
class TeamStats:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.draws = 0
        self.losses = 0

        for name in ["win", "loss", "draw"]:
            attr = name + ("es" if name[-1] == "s" else "s")
            setattr(self, 
            name, 
            # lambda attr=attr: setattr(self, attr, getattr(self, attr) + 1)
            functools.partial(
                lambda attr: setattr(self, attr, getattr(self, attr) + 1),
                attr=attr
            )
        )

    def __str__(self):
        return (
            f"{self.name.ljust(31)}| {self.matches_played:2} | {self.wins:2} | "
            f"{self.draws:2} | {self.losses:2} | {self.points:2}"
        )
        
    
    @property
    def points(self):
        return 3 * self.wins + self.draws

    @property
    def matches_played(self):
        return self.wins + self.draws + self.losses
    
    def __lt__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return (self.points, other.name) < (other.points, self.name)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return vars(self) == vars(other)


def tally(rows: list[str]) -> list[str]:
    """Returns the results of a small football competition.

    The results would be a list of rows of a table of the following form:
    Team                           | MP |  W |  D |  L |  P
    Devastating Donkeys            |  3 |  2 |  1 |  0 |  7
    Allegoric Alaskans             |  3 |  2 |  0 |  1 |  6
    Blithering Badgers             |  3 |  1 |  0 |  2 |  3
    Courageous Californians        |  3 |  0 |  1 |  2 |  1

    Parameters:
    ___________
    rows: list[str]
        A list of strings containing match resulsts. Each string is of the following
        form:
        "team_1_name;team_2_name;match_result"
        `match_result` can be either "win", "loss" or "draw"
        A win is awarded 3 points, a draw 1 point and a loss 0 points.

    Returns:
    ________
    list[str]
        Rows of the result table described above.
    """
    teams = {}
    for row in rows:
        team_1, team_2, result = row.split(";")
        team_1 = teams.setdefault(team_1, TeamStats(name=team_1))
        team_2 = teams.setdefault(team_2, TeamStats(name=team_2))

        if result == "win":
            team_1.win()
            team_2.loss()
        elif result == "loss":
            team_1.loss()
            team_2.win()
        else:
            team_1.draw()
            team_2.draw()

    ranked_teams = [str(team) for team in sorted(teams.values(), reverse=True)]
    return HEADER + ranked_teams
    