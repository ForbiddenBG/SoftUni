class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += (room.room_cost + room.expenses)
        return f"Monthly consumptions: {total_consumption:.2f}$."

    def pay(self):
        result = ""
        for room in self.rooms:
            total_exp = room.expenses + room.room_cost
            new_budget = room.budget - total_exp
            if total_exp <= room.budget:
                room.budget = new_budget
                result += f"{room.family_name} paid {total_exp:.2f}$ and have {room.budget:.2f}$ left.\n"
            else:
                family_name = room.family_name
                self.rooms.remove(room)
                result += f"{family_name} does not have enough budget and must leave the hotel.\n"
        return result.strip()

    def status(self):
        result = f"Total population: {sum([x.members_count for x in self.rooms])}\n"
        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count}" \
                      f" members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            if room.children:
                for num, child in enumerate(room.children):
                    result += f"--- Child {num+1} monthly cost: {child.get_monthly_expense():.2f}$\n"
            result += f"--- Appliances monthly cost: {sum([x.get_monthly_expense() for x in room.appliances]):.2f}$\n"
        return result.strip()
