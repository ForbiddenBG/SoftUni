class Hardware:
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.left_capacity = capacity
        self.left_memory = memory

    def install(self, software):
        if software.capacity_consumption <= self.left_capacity and software.memory_consumption <= self.left_memory:
            self.left_capacity -= software.capacity_consumption
            self.left_memory -= software.memory_consumption
            self.software_components.append(software)
        else:
            raise Exception('Software cannot be installed')

    def uninstall(self, software):
        self.software_components.remove(software)
