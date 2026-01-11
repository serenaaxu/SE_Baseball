from dataclasses import dataclass

@dataclass
class Team:
    id: int
    team_code : str
    name : str

    tot_salary : float = 0.0

    def __str__(self):
        return f"{self.name} ({self.id})"

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Team):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)
