# Component interface
class Coffee:
    def cost(self):
        pass


# Concrete component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5


# Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()


# Concrete decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2


class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1


class WhipDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 3


# Client code
def main():
    # Creating a simple coffee
    my_coffee = SimpleCoffee()
    print(f"Cost of simple coffee: ${my_coffee.cost()}")

    # Adding milk to the coffee
    my_coffee_with_milk = MilkDecorator(my_coffee)
    print(f"Cost of coffee with milk: ${my_coffee_with_milk.cost()}")

    # Adding sugar and whip to the coffee
    my_coffee_with_milk_sugar_whip = WhipDecorator(SugarDecorator(my_coffee))
    print(
        f"Cost of coffee with milk, sugar, and whip: ${my_coffee_with_milk_sugar_whip.cost()}"
    )


if __name__ == "__main__":
    main()
