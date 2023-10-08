from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    RED_BULL_SPONSORS = ["Petronas", "TeamViewer"]

    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos):
        earned_money = 0
        for sponsor in MercedesTeam.RED_BULL_SPONSORS:
            if sponsor == "Petronas":
                if race_pos <= 1:
                    earned_money += 1000000
                elif race_pos <= 3:
                    earned_money += 500000
            elif sponsor == "TeamViewer":
                if race_pos <= 5:
                    earned_money += 100000
                elif race_pos <= 7:
                    earned_money += 50000
        revenue = earned_money - 200000
        self.budget += revenue
        return f"The revenue after the race is { revenue }$. Current budget { self.budget }$"
