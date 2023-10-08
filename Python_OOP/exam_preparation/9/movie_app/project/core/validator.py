class Validator:

    @staticmethod
    def if_the_string_is_empty(value, error):
        if value.strip() == "":
            raise ValueError(error)

    @staticmethod
    def if_the_value_is_under_limit(value, age, error):
        if value < age:
            raise ValueError(error)

    @staticmethod
    def if_the_movie_was_released_under_the_year_1888(value, error):
        if value < 1888:
            raise ValueError(error)

    @staticmethod
    def if_the_atribute_is_not_an_object(value, value_obj, error):
        if not isinstance(value, value_obj):
            raise ValueError(error)
