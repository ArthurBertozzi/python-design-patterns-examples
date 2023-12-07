# Subject (Observable) - WeatherStation
class WeatherStation:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, temperature, humidity, pressure):
        for observer in self._observers:
            observer.update(temperature, humidity, pressure)


# Observer - DisplayDevice
class DisplayDevice:
    def update(self, temperature, humidity, pressure):
        pass


# Concrete Observer - PhoneDisplay
class PhoneDisplay(DisplayDevice):
    def update(self, temperature, humidity, pressure):
        print(f"Phone Display: Temperature={temperature}, Humidity={humidity}, Pressure={pressure}")


# Concrete Observer - TVDisplay
class TVDisplay(DisplayDevice):
    def update(self, temperature, humidity, pressure):
        print(f"TV Display: Temperature={temperature}, Humidity={humidity}, Pressure={pressure}")


# Usage
if __name__ == "__main__":
    # Create WeatherStation
    weather_station = WeatherStation()

    # Create Observers (Display Devices)
    phone_display = PhoneDisplay()
    tv_display = TVDisplay()

    # Add Observers to WeatherStation
    weather_station.add_observer(phone_display)
    weather_station.add_observer(tv_display)

    # Simulate Weather Changes and Notify Observers
    weather_station.notify_observers(25, 60, 1010)

    # Output:
    # Phone Display: Temperature=25, Humidity=60, Pressure=1010
    # TV Display: Temperature=25, Humidity=60, Pressure=1010
