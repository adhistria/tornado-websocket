from tornado import ioloop, web, options, httpserver
from repositories.message_repository import MessageRepository
from services.message_service import MessageService
from handlers.message_handler import MessageHandler, RealTimeMessageHandler
from handlers.page_handler import IndexHandler
import logging
import tornado

TEMPLATE_PATH = './templates'
PORT = 8000


def main():
    tornado.options.parse_command_line()
    message_repository = MessageRepository()
    message_service = MessageService(message_repository)

    app = tornado.web.Application(handlers=[
        (r"/real-time-message", RealTimeMessageHandler),
        (r"/", IndexHandler),
        (r"/message", MessageHandler, {'message_service': message_service}),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {'path': TEMPLATE_PATH}),
    ],
        template_path=TEMPLATE_PATH
    )
    server = tornado.httpserver.HTTPServer(app)
    server.bind(PORT)
    server.start()
    logging.info('Server Start')
    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
