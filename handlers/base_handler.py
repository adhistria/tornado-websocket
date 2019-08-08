import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    FAIL_STATUS = False
    SUCCESS_STATUS = True

    def success(self, data):
        data = {
            'data': data,
            'success': True,
        }
        self.set_status(200)
        self.write(data)

    def error(self):
        data = {'data': None, 'success': False}
        self.set_status(500)
        self.write(data)
