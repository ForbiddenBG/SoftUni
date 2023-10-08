class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([x.guests for x in self.rooms if x.is_taken])

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number][0]
        room.take_room(people)

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        room.free_room()

    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests\nFree rooms: " \
                 f"{', '.join([str(x.number) for x in self.rooms if not x.is_taken])}" + "\n"
        result += f"Taken rooms: {', '.join([str(x.number) for x in self.rooms if x.is_taken])}"
        return result
