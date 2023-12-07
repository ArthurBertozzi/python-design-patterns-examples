class Character:
    def __init__(self, symbol):
        self.symbol = symbol

    def display(self, font_size):
        print(f"Character {self.symbol} with font size {font_size}")


class TextEditor:
    def __init__(self):
        self.characters = {}

    def add_character(self, symbol, font_size):
        # Check if the character already exists in the pool
        if symbol not in self.characters:
            # If not, create a new character and store it in the pool
            self.characters[symbol] = Character(symbol)

        # Display the character using the shared flyweight
        self.characters[symbol].display(font_size)


# Client code
if __name__ == "__main__":
    text_editor = TextEditor()

    # Add characters to the text editor
    text_editor.add_character('A', 12)
    text_editor.add_character('B', 14)
    text_editor.add_character('A', 12)  # Reusing 'A' character

    text_editor.add_character('C', 16)
    text_editor.add_character('B', 14)  # Reusing 'B' character

    text_editor.add_character('D', 18)

