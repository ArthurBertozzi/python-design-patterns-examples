from abc import ABC, abstractmethod

# Abstract class defining the template for making a beverage
class BeverageTemplate(ABC):

    def make_beverage(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    @abstractmethod
    def boil_water(self):
        pass

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def pour_in_cup(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

# Concrete subclass for making tea
class Tea(BeverageTemplate):

    def boil_water(self):
        print("Boiling water for tea")

    def brew(self):
        print("Brewing tea leaves")

    def pour_in_cup(self):
        print("Pouring tea into cup")

    def add_condiments(self):
        print("Adding lemon to tea")

# Concrete subclass for making coffee
class Coffee(BeverageTemplate):

    def boil_water(self):
        print("Boiling water for coffee")

    def brew(self):
        print("Brewing coffee grounds")

    def pour_in_cup(self):
        print("Pouring coffee into cup")

    def add_condiments(self):
        print("Adding sugar and milk to coffee")

# Client code
def main():
    print("Making tea:")
    tea = Tea()
    tea.make_beverage()

    print("\nMaking coffee:")
    coffee = Coffee()
    coffee.make_beverage()

if __name__ == "__main__":
    main()
