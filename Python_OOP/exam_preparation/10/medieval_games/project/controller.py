def find_player_by_name(name, my_list):
    for player in my_list:
        if name == player.name:
            return player


def find_last_supply(sustenance_type, my_list):
    for idx in range(len(my_list)-1, -1, -1):
        if my_list[idx].__class__.__name__ == sustenance_type:
            return my_list.pop(idx)


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        my_list = []
        for player in args:
            if player not in self.players:
                my_list.append(player)
                self.players.append(player)
        return f"Successfully added: {', '.join([x.name for x in my_list])}"

    def add_supply(self, *args):
        self.supplies.extend(args)

    def sustain(self, player_name, sustenance_type):
        if sustenance_type in "FoodDrink":
            player = find_player_by_name(player_name, self.players)

            if sustenance_type == "Food" and not [x for x in self.supplies if x.__class__.__name__ == "Food"]:
                raise Exception("There are no food supplies left!")
            if sustenance_type == "Drink" and not [x for x in self.supplies if x.__class__.__name__ == "Drink"]:
                raise Exception("There are no drink supplies left!")

            if player:
                if player.need_sustenance:
                    last_supply = find_last_supply(sustenance_type, self.supplies)
                    if player.stamina + last_supply.energy > 100:
                        player.stamina = 100
                    else:
                        player.stamina += last_supply.energy
                    return f"{player.name} sustained successfully with {last_supply.name}."
                else:
                    return f"{player.name} have enough stamina."

    def duel(self, first_player_name, second_player_name):
        first_player = find_player_by_name(first_player_name, self.players)
        second_player = find_player_by_name(second_player_name, self.players)

        players = [first_player, second_player]

        zero_stamina = ""
        for player in players:
            if player.stamina == 0:
                zero_stamina += f"Player {player.name} does not have enough stamina." + "\n"
        if zero_stamina:
            return zero_stamina.strip()

        sorted_by_lower_stamina = sorted(players, key=lambda x: x.stamina)
        winner_name = ""

        for player in sorted_by_lower_stamina:
            current_defender = [x for x in players if x != player][0]
            if current_defender.stamina - player.stamina / 2 < 0:
                current_defender.stamina = 0
                winner_name = player.name
                break
            else:
                current_defender.stamina -= player.stamina / 2

        if winner_name:
            return f"Winner: {winner_name}"
        else:
            sorted_winner_by_stamina = sorted(players, key=lambda x: -x.stamina)[0]
            return f"Winner: {sorted_winner_by_stamina.name}"

    def next_day(self):
        for player in self.players:
            reduce_value = player.age * 2
            if player.stamina - reduce_value < 0:
                player.stamina = 0
            else:
                player.stamina -= reduce_value
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = ""
        for x in self.players:
            result += f"{x.__str__()}" + '\n'
        for j in self.supplies:
            result += f"{j.details()}" + '\n'
        return result.strip()
