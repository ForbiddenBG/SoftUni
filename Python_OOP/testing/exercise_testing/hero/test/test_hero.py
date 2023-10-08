from unittest import TestCase, main

from project.hero import Hero


class HeroTest(TestCase):
    def test_initialized_correctly_constructor(self):
        hero = Hero("Div", 10, 100.0, 100.0)
        self.assertEqual("Div", hero.username)
        self.assertEqual(10, hero.level)
        self.assertEqual(100.0, hero.health)
        self.assertEqual(100.0, hero.damage)

    def test_battle_you_cannot_fight_with_yourself_raises(self):
        hero = Hero("Div", 10, 100.0, 100.0)
        with self.assertRaises(Exception) as ex:
            hero.battle(hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_with_lower_health_equal_to_zero_raises(self):
        hero = Hero("Max", 10, 0, 100.0)
        enemy = Hero("Lex", 10, 20, 100)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_hero_with_lower_health_less_than_zero_raises(self):
        hero = Hero("Max", 10, -20, 100.0)
        enemy = Hero("Lex", 10, 20, 100)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_with_lower_health_equal_to_zero_raises(self):
        hero = Hero("Max", 10, 20, 100.0)
        enemy = Hero("Lex", 10, 0, 100)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy)
        self.assertEqual("You cannot fight Lex. He needs to rest", str(ex.exception))

    def test_battle_enemy_with_lower_health_less_than_zero_raises(self):
        hero = Hero("Max", 10, 20, 100.0)
        enemy = Hero("Lex", 10, -20, 100)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy)
        self.assertEqual("You cannot fight Lex. He needs to rest", str(ex.exception))

    def test_initiating_valid_battle_hero_win_with_enemy_health_zero(self):
        hero = Hero("Max", 1, 20, 10)
        enemy = Hero("Lex", 1, 10, 10)
        result = hero.battle(enemy)
        self.assertEqual("You win", result)
        self.assertEqual(2, hero.level)
        self.assertEqual(15, hero.health)
        self.assertEqual(15, hero.damage)

    def test_initiating_valid_battle_hero_win_with_enemy_health_less_than_zero(self):
        hero = Hero("Max", 1, 20, 100)
        enemy = Hero("Lex", 1, 10, 10)
        result = hero.battle(enemy)
        self.assertEqual("You win", result)
        self.assertEqual(2, hero.level)
        self.assertEqual(15, hero.health)
        self.assertEqual(105, hero.damage)

    def test_initiating_valid_battle_enemy_win_with_hero_health_zero(self):
        hero = Hero("Max", 1, 10, 10)
        enemy = Hero("Lex", 1, 20, 10)
        result = hero.battle(enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(2, enemy.level)
        self.assertEqual(15, enemy.health)
        self.assertEqual(15, enemy.damage)

    def test_initiating_valid_battle_enemy_win_with_hero_health_less_than_zero(self):
        hero = Hero("Max", 1, 10, 10)
        enemy = Hero("Lex", 1, 20, 100)
        result = hero.battle(enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(2, enemy.level)
        self.assertEqual(15, enemy.health)
        self.assertEqual(105, enemy.damage)

    def test_initiating_valid_draw_battle_with_zero_health(self):
        hero = Hero("Max", 1, 20, 20)
        enemy = Hero("Lex", 1, 20, 20)
        result = hero.battle(enemy)
        self.assertEqual("Draw", result)

    def test_initiating_valid_draw_battle_less_health(self):
        hero = Hero("Max", 1, 20, 200)
        enemy = Hero("Lex", 1, 20, 200)
        result = hero.battle(enemy)
        self.assertEqual("Draw", result)

    def test_return_correctly_dunder_str(self):
        hero = Hero("Max", 20, 20, 200)
        result = f"Hero Max: 20 lvl\n" \
                   f"Health: 20\n" \
                   f"Damage: 200\n"
        self.assertEqual(result, hero.__str__())


if __name__ == "__main__":
    main()
