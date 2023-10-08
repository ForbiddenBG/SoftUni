class Validator:
    @staticmethod
    def raises_if_the_number_does_not_start_with_0_and_len_is_not_10(value, error):
        if value[0] != "0" or len(value) < 10 or not value.isdigit():
            raise ValueError(error)

    @staticmethod
    def raises_if_the_value_is_empty_string(value, error):
        if value.strip() == "":
            raise ValueError(error)

    @staticmethod
    def raises_if_the_value_is_less_than_or_equal_to_zero(value, error):
        if value <= 0:
            raise ValueError(error)
