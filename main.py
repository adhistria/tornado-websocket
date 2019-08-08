from tornado import ioloop, web, options, httpserver
from repositories.message_repository import MessageRepository
from services.message_service import MessageService
from handlers.message_handler import MessageHandler
import tornado


def main():
    tornado.options.parse_command_line()
    message_repository = MessageRepository()
    message_service = MessageService(message_repository)

    app = tornado.web.Application(handlers=[
        (r"/message", MessageHandler, {'message_service': message_service}),
    ])
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8000)
    server.start(0)
    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
