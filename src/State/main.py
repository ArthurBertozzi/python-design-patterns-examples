# Define the interface for the states
class VendingMachineState:
    def insert_money(self):
        pass

    def eject_money(self):
        pass

    def select_item(self):
        pass

    def dispense_item(self):
        pass


# Implement concrete states
class NoMoneyState(VendingMachineState):
    def insert_money(self):
        print("Money inserted")
        return HasMoneyState()

    def eject_money(self):
        print("No money to eject")

    def select_item(self):
        print("Please insert money first")

    def dispense_item(self):
        print("Please insert money and select item first")


class HasMoneyState(VendingMachineState):
    def insert_money(self):
        print("Money already inserted")

    def eject_money(self):
        print("Money ejected")
        return NoMoneyState()

    def select_item(self):
        print("Item selected")
        return SoldState()

    def dispense_item(self):
        print("Please select item first")


class SoldState(VendingMachineState):
    def insert_money(self):
        print("Item already sold, cannot insert money")

    def eject_money(self):
        print("Item dispensed, cannot eject money")

    def select_item(self):
        print("Item already selected, wait for dispensing")

    def dispense_item(self):
        print("Item dispensed")
        return NoMoneyState()


# Context class representing the Vending Machine
class VendingMachine:
    def __init__(self):
        # Initial state is NoMoneyState
        self.state = NoMoneyState()

    def insert_money(self):
        self.state = self.state.insert_money()

    def eject_money(self):
        self.state = self.state.eject_money()

    def select_item(self):
        self.state = self.state.select_item()

    def dispense_item(self):
        self.state = self.state.dispense_item()


# Example usage
if __name__ == "__main__":
    vending_machine = VendingMachine()

    vending_machine.select_item()  # Output: Please insert money first

    vending_machine.insert_money()  # Output: Money inserted
    vending_machine.select_item()  # Output: Item selected

    vending_machine.insert_money()  # Output: Money already inserted
    vending_machine.eject_money()   # Output: Money ejected

    vending_machine.dispense_item()  # Output: Item dispensed
    vending_machine.select_item()     # Output: Please insert money first
