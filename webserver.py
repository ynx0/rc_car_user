import falcon
from procbridge.procbridge import *

# MARK - hardware_server procbridge settings
host = '192.168.0.125' # put correct ip of pi
port = 9009
client = ProcBridge(host, port)

# MARK - utility methods

# def validate_params(params):
#     if params == {} or params[0] == None or


# MARK - falcon server handler code

class MoveHandler(object):

    def on_post(self, req, resp):
        print('=============')
        print('params: %s' % req.params)
        params = list(req.params)
        #validate_params(params)
        cmd = params[0]
        p1 = params[1]
        print('cmd is: %s' % cmd)
        print('param1 is: %s' % p1)
        try:
            #client.request(cmd, p1)
            resp.status = falcon.HTTP_200
            resp.body = 'Command received: cmd: %s' % (cmd)
        except TimeoutError:
            resp.status = falcon.HTTP_500


    # try:
    #     client.request(cmd, param1)
    # except Exception as e:
    #     success = "Failed: " + str(e)



app = falcon.API()
app.req_options.auto_parse_form_urlencoded = True
app.add_route('/move', MoveHandler())

#
# def start():
#     app.add_route('/move', MoveHandler)
#     while True:
#         pass
#
# if __name__ == '__main__':
#     try:
#         start()
#     except KeyboardInterrupt:
#         print("Stopping webserver")
