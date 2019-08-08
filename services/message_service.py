class MessageService(object):
    def __init__(self, message_repository):
        self.message_repository = message_repository

    def get_messages(self):
        return self.message_repository.find_all()
