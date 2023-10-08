class Validator:

    @staticmethod
    def the_string_is_empty_or_contains_white_spaces(value, error):
        if value.strip() == "":
            raise ValueError(error)

    @staticmethod
    def the_value_is_under_eighteen(value, error):
        if value < 18:
            raise ValueError(error)

    @staticmethod
    def the_string_len_is_under_four_symbols(value, error):
        if len(value) < 4:
            raise ValueError(error)

    @staticmethod
    def the_speed_exceeded_the_max_speed(value, max_horse_speed, error):
        if value > max_horse_speed:
            raise ValueError(error)

    @staticmethod
    def the_race_type_is_not_in_the_available_races(value, my_list, error):
        if value not in my_list:
            raise ValueError(error)
