class Town:
    def __init__(self, name):
        self.name = name
        self.latitude = None
        self.longitude = None

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"


# town = Town("Sofia")
# town.set_latitude()
# town.set_longitude()
# print(town)
