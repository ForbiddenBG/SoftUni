class Validator:

    @staticmethod
    def the_model_is_less_than_four_symbols(value, error):
        if len(value) < 4:
            raise ValueError(error)

    @staticmethod
    def the_speed_is_out_of_the_valid_range(value, error, min_speed, max_speed):
        if value < min_speed or value > max_speed:
            raise ValueError(error)

    @staticmethod
    def if_name_contains_empty_string_or_white_spaces(value, error):
        if value.strip() == "":
            raise ValueError(error)

