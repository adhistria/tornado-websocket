class MessageRepository(object):

    def __init__(self):
        self._messages = []

    def find_all(self):
        return self._messages

    def save(self, message):
        self._messages.append(message)
        return message
