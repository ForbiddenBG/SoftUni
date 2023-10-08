from abc import ABC, abstractmethod

from project.core.validator import Validator


class Table(ABC):
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False
        
    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        Validator.if_is_equal_or_less_than_0(value, "Capacity has to be greater than 0!")
        self.__capacity = value

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        Validator.raise_if_the_number_is_out_of_range(value, self.min_num, self.max_num, self.error_massage)
        self.__table_number = value

    @property
    @abstractmethod
    def min_num(self):
        pass

    @property
    @abstractmethod
    def max_num(self):
        pass

    @property
    @abstractmethod
    def error_massage(self):
        pass
        
    def reserve(self, number_of_people):
        if self.capacity >= number_of_people:
            self.number_of_people = number_of_people
            self.is_reserved = True

    def order_food(self, baked_food):
        self.food_orders.append(baked_food)

    def order_drink(self, drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        total_bill = sum([x.price for x in self.food_orders]) + sum([x.price for x in self.drink_orders])
        return total_bill

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            result = f"Table: {self.table_number}\n"
            result += f"Type: {self.__class__.__name__}\n"
            result += f"Capacity: {self.capacity}"
            return result

