from .base_handler import BaseHandler
import tornado.websocket
from tornado import ioloop
import json
import logging


class MessageHandler(BaseHandler):
    def initialize(self, message_service) -> None:
        self._message_service = message_service

    def get(self):
        messages = self._message_service.get_messages()
        self.success(messages)

    def post(self):
        try:
            body = json.loads(self.request.body)
            message = body['message']
            server = ioloop.IOLoop.current()
            server.add_callback(RealTimeMessageHandler.send_message, message)
            reponse = self._message_service.store(message)
            self.success(reponse)
        except:
            self.error()


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
