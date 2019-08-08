import tornado.web
import tornado.websocket
from tornado import ioloop
import json
import logging


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
            server = ioloop.IOLoop.current()
            server.add_callback(RealTimeMessageHandler.send_message, message)
            reponse = self._message_service.store(message)
            data = {'data': reponse, 'success': True}
            self.set_status(200)
            self.write(data)
        except:
            data = {'data': None, 'success': False}
            self.write(data)
            self.set_status(500)


class RealTimeMessageHandler(tornado.websocket.WebSocketHandler):
    live_web_sockets = set()

    def open(self):
        logging.info("Client Connected")
        self.live_web_sockets.add(self)

    def on_close(self):
        logging.info("Client Disconnected")

    def on_message(self, message):
        logging.info("Send Message: {}".format(message))

    @classmethod
    def send_message(cls, message):
        for web_socket in cls.live_web_sockets:
            if web_socket.ws_connection and web_socket.ws_connection.stream.socket:
                web_socket.write_message(message)
