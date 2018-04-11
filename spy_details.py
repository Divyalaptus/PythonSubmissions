from datetime import datetime
class Spy:

    def __init__(self, name, salutation, age, rating):
        # Initializing the values
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None
        # Count the number of words
        self.count = 0

# a class for chat_messages
class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Divyansh', 'Mr.', 20, 4.5)

friend_one = Spy('Himalaya', 'Mr.', 27, 4.8)
friend_two = Spy('Vaibhav', 'Mr.', 21, 4.9)
friend_three = Spy('Sachin', 'Mr.', 27 , 4.9)

# List of friends
friends = [friend_one, friend_two, friend_three]