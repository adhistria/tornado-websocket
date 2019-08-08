import tornado.web


class MessageHandler(tornado.web.RequestHandler):
    def initialize(self, message_service) -> None:
        self._message_service = message_service

    def get(self):
        messages = self._message_service.get_messages()
        data = {
            'data': messages,
            'success': True
        }
        self.set_status(200)
        self.write(data)
