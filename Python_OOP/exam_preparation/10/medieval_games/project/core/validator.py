class Validator:

    @staticmethod
    def energy_is_less_than_zero(value, error):
        if value < 0:
            raise ValueError(error)

    @staticmethod
    def the_player_age_is_under_12(value, error):
        if value < 12:
            raise ValueError(error)

    @staticmethod
    def the_stamina_is_less_or_above_the_limits(value, error):
        if value < 0 or value > 100:
            raise ValueError(error)
