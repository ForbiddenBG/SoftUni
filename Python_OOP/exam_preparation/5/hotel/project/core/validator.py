class Validator:

    @staticmethod
    def raise_if_the_value_is_set_to_a_negative_number(value, error):
        if value < 0:
            raise ValueError(error)
