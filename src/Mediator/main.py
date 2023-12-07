class Mediator:
    def send_message(self, message, user):
        pass


class ChatRoomMediator(Mediator):
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, user):
        for u in self.users:
            if u != user:
                u.receive(message)


class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send(self, message):
        print(f"{self.name} sends: {message}")
        self.mediator.send_message(message, self)

    def receive(self, message):
        print(f"{self.name} receives: {message}")


# Usage example
if __name__ == "__main__":
    # Create mediator (chat room)
    chat_room = ChatRoomMediator()

    # Create users
    user1 = User("User1", chat_room)
    user2 = User("User2", chat_room)
    user3 = User("User3", chat_room)

    # Add users to the chat room
    chat_room.add_user(user1)
    chat_room.add_user(user2)
    chat_room.add_user(user3)

    # Users send and receive messages through the mediator
    user1.send("Hello, everyone!")
    user2.send("Hi, User1!")
    user3.send("Greetings!")

