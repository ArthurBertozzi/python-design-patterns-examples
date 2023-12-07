import copy

"""

The prototype design pattern is a creational design pattern that allows the creation of objects based on an existing object, known as the prototype. This pattern involves creating new objects by copying an existing object, known as the prototype.

Here's a simple example in Python to illustrate the prototype design pattern. Let's create a prototype class representing a car, and then create new car objects by cloning the prototype:


In this example, we have a CarPrototype class with attributes model 
and color. The clone method uses the copy.copy function to 
create a shallow copy of the object. 
We then create a prototype car and clone it to create two new cars. B
y modifying the attributes of the cloned cars, we can see that the
changes do not affect the prototype or other cloned cars.

This demonstrates how the prototype design pattern can be used to create new objects by copying an existing prototype, providing a flexible way to create and configure objects based on an existing instance.
"""


class CarPrototype:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def clone(self):
        # Using the built-in copy method to create a shallow copy
        return copy.copy(self)


# Client code
if __name__ == "__main__":
    # Create a prototype car
    prototype_car = CarPrototype(model="Sedan", color="Blue")

    # Clone the prototype to create new cars
    car1 = prototype_car.clone()
    car2 = prototype_car.clone()

    # Modify the cloned cars
    car1.color = "Red"
    car2.model = "SUV"

    # Display the information of each car
    print("Prototype Car:", prototype_car.model, prototype_car.color)
    print("Car 1:", car1.model, car1.color)
    print("Car 2:", car2.model, car2.color)
