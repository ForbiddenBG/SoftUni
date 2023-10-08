class Validator:

    @staticmethod
    def is_empty_string_or_white_spaces(value, error):
        if value.strip() == "":
            raise ValueError(error)
