from services.message_service import MessageService
from unittest import mock
import unittest


class TestMessageService(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_image_repository = mock.Mock()

    def test_get_messages_when_message_in_repository_empty(self):
        message_service = MessageService(self.mock_image_repository)

        self.mock_image_repository.find_all.return_value = []
        messages = message_service.get_messages()

        expected_message = []
        self.assertEqual(messages, expected_message)
