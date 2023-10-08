class Validator:

    @staticmethod
    def raise_if_it_is_an_empty_string(value, error):
        if value.strip() == "":
            raise ValueError(error)

    @staticmethod
    def raise_if_the_value_is_below_or_equal_to_0(value, error):
        if value <= 0:
            raise ValueError(error)
