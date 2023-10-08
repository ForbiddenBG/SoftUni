class Validator:
    @staticmethod
    def is_empty_string_or_white_space(value, error):
        if value.strip() == "":
            raise ValueError(error)

    @staticmethod
    def if_is_equal_or_less_than_0(value, error):
        if value <= 0:
            raise ValueError(error)

    @staticmethod
    def raise_if_the_number_is_out_of_range(value, min_num, max_num, error):
        if value < min_num or value > max_num:
            raise ValueError(error)
