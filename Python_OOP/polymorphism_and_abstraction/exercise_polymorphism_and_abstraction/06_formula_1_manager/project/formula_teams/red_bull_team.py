from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    RED_BULL_SPONSORS = ["Oracle", "Honda"]

    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos):
        earned_money = 0
        for sponsor in RedBullTeam.RED_BULL_SPONSORS:
            if sponsor == "Oracle":
                if race_pos <= 1:
                    earned_money += 1500000
                elif race_pos <= 2:
                    earned_money += 800000
            elif sponsor == "Honda":
                if race_pos <= 8:
                    earned_money += 20000
                elif race_pos <= 10:
                    earned_money += 10000
        revenue = earned_money - 250000
        self.budget += revenue
        return f"The revenue after the race is { revenue }$. Current budget { self.budget }$"
