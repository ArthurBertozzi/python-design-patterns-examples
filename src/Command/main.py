from abc import ABC, abstractmethod

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# ConcreteCommand classes
class TVOnCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_on()

class TVOffCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_off()

# Receiver class
class TV:
    def turn_on(self):
        print("TV is ON")

    def turn_off(self):
        print("TV is OFF")

# Invoker class
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

# Client code
if __name__ == "__main__":
    # Creating instances
    tv = TV()
    on_command = TVOnCommand(tv)
    off_command = TVOffCommand(tv)

    # Creating invoker and associating commands
    remote = RemoteControl()
    remote.set_command(on_command)

    # Pressing the button to turn on the TV
    remote.press_button()

    # Changing the command to turn off the TV
    remote.set_command(off_command)

    # Pressing the button to turn off the TV
    remote.press_button()
