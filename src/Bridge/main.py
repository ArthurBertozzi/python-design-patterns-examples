# Abstraction
class RemoteControl:
    def __init__(self, device):
        self.device = device

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()


# Implementor
class Device:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


# Concrete Implementor 1
class TV(Device):
    def turn_on(self):
        print("Turning on the TV")

    def turn_off(self):
        print("Turning off the TV")


# Concrete Implementor 2
class Radio(Device):
    def turn_on(self):
        print("Turning on the Radio")

    def turn_off(self):
        print("Turning off the Radio")


# Client code
if __name__ == "__main__":
    tv = TV()
    radio = Radio()

    remote_tv = RemoteControl(tv)
    remote_tv.turn_on()
    remote_tv.turn_off()

    remote_radio = RemoteControl(radio)
    remote_radio.turn_on()
    remote_radio.turn_off()
