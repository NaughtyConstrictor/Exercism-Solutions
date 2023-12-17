HEADER = ["Team                           | MP |  W |  D |  L |  P"]


class TeamStats:
    def __init__(self, name):
        self.name = name
        self.matches_played = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        
    def __str__(self):
        return (
            f"{self.name.ljust(31)}| {str(self.matches_played).rjust(2)} | "
            f"{str(self.wins).rjust(2)} | {str(self.draws).rjust(2)} | "
            f"{str(self.losses).rjust(2)} | {str(self.points).rjust(2)}"
        )

    def win(self):
        self.wins += 1

    def loss(self):
        self.losses += 1

    def draw(self):
        self.draws += 1

    @property
    def points(self):
        return 3 * self.wins + self.draws

    def __getattribute__(self, name):
        if name in ["win", "loss", "draw"]:
            self.matches_played += 1
        return object.__getattribute__(self, name)

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return (self.points, other.name) < (other.points, self.name)


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
        if team_1 not in teams:
            teams[team_1] = TeamStats(name=team_1)
        if team_2 not in teams:
            teams[team_2] = TeamStats(name=team_2)
        
        if result == "win":
            teams[team_1].win()
            teams[team_2].loss()
        elif result == "loss":
            teams[team_1].loss()
            teams[team_2].win()
        else:
            teams[team_1].draw()
            teams[team_2].draw()

    ranked_teams = [str(team) for team in sorted(teams.values(), reverse=True)]
    return HEADER + ranked_teams
    