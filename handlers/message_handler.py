import tornado.web
import json


class MessageHandler(tornado.web.RequestHandler):
    def initialize(self, message_service) -> None:
        self._message_service = message_service

    def get(self):
        messages = self._message_service.get_messages()
        data = {
            'data': messages,
            'success': True,
        }
        self.set_status(200)
        self.write(data)

    def post(self):
        try:
            body = json.loads(self.request.body)
            message = body['message']
            reponse = self._message_service.store(message)
            data = {'data': reponse, 'success': True}
            self.set_status(200)
            self.write(data)
        except:
            data = {'data': None, 'success': False}
            self.write(data)
            self.set_status(500)
