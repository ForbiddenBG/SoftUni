from project.core.Validator import Validator


class Client:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        Validator.raises_if_the_number_does_not_start_with_0_and_len_is_not_10(value, "Invalid phone number!")
        self.__phone_number = value
