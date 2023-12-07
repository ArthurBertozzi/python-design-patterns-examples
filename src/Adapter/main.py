# Adaptee 1: Celsius temperature class
class CelsiusTemperature:
    def get_temperature(self):
        return 0


# Adaptee 2: Fahrenheit temperature class
class FahrenheitTemperature:
    def get_temperature(self):
        return 32


# Target interface: Temperature interface that we want to use
class Temperature:
    def get_temperature(self):
        pass


# Adapter class to adapt CelsiusTemperature to Temperature
class CelsiusAdapter(Temperature):
    def __init__(self, celsius_temp):
        self.celsius_temp = celsius_temp

    def get_temperature(self):
        # Convert Celsius to Fahrenheit
        return (self.celsius_temp.get_temperature() * 9 / 5) + 32


# Adapter class to adapt FahrenheitTemperature to Temperature
class FahrenheitAdapter(Temperature):
    def __init__(self, fahrenheit_temp):
        self.fahrenheit_temp = fahrenheit_temp

    def get_temperature(self):
        # Convert Fahrenheit to Celsius
        return (self.fahrenheit_temp.get_temperature() - 32) * 5 / 9


# Client code
def print_temperature(temp):
    print(f"Temperature: {temp.get_temperature()}")


# Using the Adapter pattern
celsius_temp = CelsiusTemperature()
celsius_adapter = CelsiusAdapter(celsius_temp)

fahrenheit_temp = FahrenheitTemperature()
fahrenheit_adapter = FahrenheitAdapter(fahrenheit_temp)

print_temperature(celsius_adapter)  # Output: Temperature: 32.0
print_temperature(fahrenheit_adapter)  # Output: Temperature: 0.0
