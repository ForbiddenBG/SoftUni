class Validator:
    @staticmethod
    def raise_if_the_string_is_enmpty_or_whitespace(val, error):
        if val.strip() == "":
            raise ValueError(error)
