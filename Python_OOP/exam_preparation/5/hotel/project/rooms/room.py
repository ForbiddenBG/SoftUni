from project.core.validator import Validator


class Room:
    def __init__(self, family_name, budget, members_count):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        Validator.raise_if_the_value_is_set_to_a_negative_number(value, "Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        result = 0
        for x in args:
            for j in x:
                result += j.get_monthly_expense()
        self.expenses = result
