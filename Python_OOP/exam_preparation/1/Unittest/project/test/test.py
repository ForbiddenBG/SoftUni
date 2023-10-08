from unittest import TestCase, main
from project.team import Team


class TestTeam(TestCase):
    def test_correctly_initialized_constructor(self):
        team = Team("Milan")
        self.assertEqual("Milan", team.name)
        self.assertEqual({}, team.members)

    def test_valid_name_initialized(self):
        team = Team("Milan")
        team.name = "Milan"
        self.assertEqual("Milan", team.name)

    def test_invalid_name_set_with_digits_raises(self):
        team = Team("Milan")
        with self.assertRaises(ValueError) as context:
            team.name = "M!1@n"
        self.assertEqual("Team Name can contain only letters!", str(context.exception))

    def test_add_member_in_the_team_correctly(self):
        team = Team("Milan")
        team.members = {"Baggio": 20}
        players = {"Zidane": 20}
        result = team.add_member(**players)
        self.assertEqual({"Baggio": 20, "Zidane": 20}, team.members)
        self.assertEqual("Successfully added: Zidane", result)

    def test_add_player_that_already_exists(self):
        team = Team("Milan")
        team.members = {"Zidane": 20}
        players = {"Zidane": 20}
        team.add_member(**players)
        self.assertEqual({"Zidane": 20}, team.members)

    def test_removing_the_player_correctly(self):
        team = Team("Milan")
        team.members = {"Zidane": 20}
        result = team.remove_member("Zidane")
        self.assertEqual({}, team.members)
        self.assertEqual("Member Zidane removed", result)

    def test_removing_the_player_that_doesnt_exist(self):
        team = Team("Milan")
        team.members = {}
        result = team.remove_member("Zidane")
        self.assertEqual({}, team.members)
        self.assertEqual("Member with name Zidane does not exist", result)

    def test_correctly_find_the_bigger_team(self):
        team1 = Team("Milan")
        team1.members = {"Baggio": 20, "Zidane": 20}
        team2 = Team("Napoli")
        team2.members = {"Maradona": 25}
        result = team1.__gt__(team2)
        self.assertEqual(True, result)

    def test_incorrectly_find_the_bigger_team(self):
        team1 = Team("Milan")
        team1.members = {"Baggio": 20, "Zidane": 20}
        team2 = Team("Napoli")
        team2.members = {"Maradona": 25}
        result = team2.__gt__(team1)
        self.assertEqual(False, result)

    def test_correctly_find_the_bigger_team_with_equal_players(self):
        team1 = Team("Milan")
        team1.members = {"Baggio": 20}
        team2 = Team("Napoli")
        team2.members = {"Maradona": 25}
        result = team1.__gt__(team2)
        self.assertEqual(False, result)

    def test_dunder_len_correctly(self):
        team = Team("Milan")
        team.members = {"Baggio": 20, "Zidane": 20}
        result = team.__len__()
        self.assertEqual(2, result)

    def test_dunder_add_correctly(self):
        team1 = Team("Milan")
        team1.members = {"Zidane": 20}
        team2 = Team("Napoli")
        team2.members = {"Maradona": 25}
        new_team = team1.__add__(team2)
        self.assertEqual("MilanNapoli", new_team.name)
        self.assertEqual({"Zidane": 20, "Maradona": 25}, new_team.members)

    def test_dunder_str_correctly(self):
        team = Team("Milan")
        team.members = {"Maradona": 25, "Baggio": 20, "Zidane": 20}
        result = team.__str__()
        self.assertEqual("Team name: Milan\nMember: Maradona - 25-years old\nMember: Baggio - 20-years old\nMember: Zidane - 20-years old", result)


if __name__ == "__main__":
    main()