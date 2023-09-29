class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        for i in args:
            if i not in self.players:
                self.players.append(i)
        return f"Successfully added: {', '.join([x.name for x in self.players])}"

    def add_supply(self, *args):
        for i in args:
            self.supplies.append(i)

    def sustain(self, player_name, sustenance_type):
        player_list = [x for x in self.players if player_name == x.name]
        supplies_list = [x for x in self.supplies if x.__class__.__name__ == sustenance_type]
        current_player = player_list[0]
        current_supply = supplies_list[-1]
        if sustenance_type in ["Food", "Drink"]:

            if sustenance_type == "Food" and not supplies_list:
                raise Exception("There are no food supplies left!")
            if sustenance_type == "Drink" and not supplies_list:
                raise Exception("There are no drink supplies left!")
            if current_player.stamina + current_player.energy < 100:
                current_player.stamina = 100
                return f"{player_name} have enough stamina."
            current_player.stamina += current_player.energy
            self.supplies.remove(current_supply)
            return f"{player_name} sustained successfully with {current_supply.name}."

    def duel(self, first_player_name, second_player_name):
        first_player = [x for x in self.players if first_player_name == x.name]
        second_player = [x for x in self.players if second_player_name == x.name]
        first = first_player[0]
        second = second_player[0]

        players = [first, second]
        result = ""
        for p in players:
            if first.stamina == 0:
                result += f"Player {first.name} does not have enough stamina.\n"
            if second.stamina == 0:
                result += f"Player {second.name} does not have enough stamina.\n"
        if result:
            return result.strip()


        playing = sorted(players, key=lambda x: x.stamina)

        if first.stamina > 0 and second.stamina > 0:
            for i in playing:
                pass

        # return f"Winner: {i.name}"

    def next_day(self):
        for plr in self.players:
            if plr.stamina - 2*plr.age >= 0:
                plr.stamina -= plr.age*2
            else:
                plr.stamina = 0
            self.sustain(plr.name, "Food")
            self.sustain(plr.name, "Drink")

    def __str__(self):
        result = ""
        for p in self.players:
            result += f"Player: {p.name}, {p.age}, {p.stamina}, {p.need_sustenance}\n"
        for s in self.supplies:
            result += f"{s.details()}\n"
        return result.strip()


