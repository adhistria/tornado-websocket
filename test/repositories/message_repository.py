from repository.message_repository import MessageRepository
import unittest


class TestMessageRepository(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_get_data_when_message_empty(self):
        message_repository = MessageRepository()

        messages = message_repository.find_all()

        expected_message = []
        self.assertEqual(messages, expected_message)

    def test_get_data_when_message_not_empty(self):
        message_repository = MessageRepository()

        message_repository.save('New Message')
        messages = message_repository.find_all()

        expected_message = ['New Message']
        self.assertEqual(messages, expected_message)
