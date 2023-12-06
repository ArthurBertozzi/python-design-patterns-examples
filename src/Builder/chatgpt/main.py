from abc import ABC, abstractmethod

# Step 1: Define the product (Computer) and its parts (components)
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.graphics_card = None

    def __str__(self):
        return f"Computer - CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}, Graphics Card: {self.graphics_card}"


# Step 2: Define an interface for building each part of the product (Computer) using ABC
class ComputerBuilder(ABC):
    @abstractmethod
    def build_cpu(self):
        pass

    @abstractmethod
    def build_ram(self):
        pass

    @abstractmethod
    def build_storage(self):
        pass

    @abstractmethod
    def build_graphics_card(self):
        pass

    @abstractmethod
    def get_computer(self):
        pass


# Step 3: Create concrete builder classes implementing the builder interface
class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def build_cpu(self):
        self.computer.cpu = "High-end Gaming CPU"

    def build_ram(self):
        self.computer.ram = "16GB DDR4 RAM"

    def build_storage(self):
        self.computer.storage = "1TB SSD"

    def build_graphics_card(self):
        self.computer.graphics_card = "NVIDIA GeForce RTX 3080"

    def get_computer(self):
        return self.computer


class OfficeComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def build_cpu(self):
        self.computer.cpu = "Office-grade CPU"

    def build_ram(self):
        self.computer.ram = "8GB DDR4 RAM"

    def build_storage(self):
        self.computer.storage = "500GB HDD"

    def build_graphics_card(self):
        self.computer.graphics_card = "Integrated Graphics"

    def get_computer(self):
        return self.computer


# Step 4: Create a Director class to orchestrate the construction process
class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_computer(self):
        self.builder.build_cpu()
        self.builder.build_ram()
        self.builder.build_storage()
        self.builder.build_graphics_card()

    def get_computer(self):
        return self.builder.get_computer()


# Step 5: Client code that uses the Director and Builder to create a specific type of computer
gaming_builder = GamingComputerBuilder()
office_builder = OfficeComputerBuilder()

gaming_director = ComputerDirector(gaming_builder)
office_director = ComputerDirector(office_builder)

gaming_director.construct_computer()
office_director.construct_computer()

gaming_computer = gaming_director.get_computer()
office_computer = office_director.get_computer()

print("Gaming Computer:")
print(gaming_computer)

print("\nOffice Computer:")
print(office_computer)
