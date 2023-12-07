# Originator: TextEditor
class TextEditor:
    def __init__(self):
        self.text = ""

    def write(self, text):
        self.text += text

    def save(self):
        return TextEditorMemento(self.text)

    def restore(self, memento):
        self.text = memento.get_state()

    def __str__(self):
        return f"Text: {self.text}"

# Memento: TextEditorMemento
class TextEditorMemento:
    def __init__(self, state):
        self.state = state

    def get_state(self):
        return self.state

# Caretaker: History
class History:
    def __init__(self):
        self.states = []

    def push(self, state):
        self.states.append(state)

    def pop(self):
        if self.states:
            return self.states.pop()
        return None

# Client Code
if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    editor.write("Hello, ")
    history.push(editor.save())  # Save state

    editor.write("world!")
    history.push(editor.save())  # Save state

    print("Current state:")
    print(editor)

    print("\nUndo one step:")
    editor.restore(history.pop())  # Undo
    print(editor)
