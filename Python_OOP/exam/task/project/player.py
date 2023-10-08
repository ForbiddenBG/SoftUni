class Player:
    def __init__(self, name, age, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina
        self._need_sustenance = False
        self.players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")
        if value in self.players:
            raise Exception(f"Name {value} is already used!")
        self.__name = value
        self.players.append(value)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if 0 > value > 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = value
        
    @property
    def need_sustenance(self):
        if self.stamina < 100:
            return True

    def __str__(self):
        return f"Player: {self.__name__}, {self.age}, {self.stamina}, {self._need_sustenance}"
