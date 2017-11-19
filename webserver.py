from bottle import *
from procbridge.procbridge import *

# MARK - hardware_server procbridge settings
host = '127.0.0.1' # TODO - put correct ip of pi
port = 9939
client = ProcBridge(host, port)

# MARK - Bottle http server code
app = Bottle()


@app.post('/move')
def handle_web_command():
    print("Post from: " + str(request.remote_addr))
    cmd = request.forms.get('cmd')
    param1 = request.forms.get('p1')
    success = "OK"

    print("CMD: %s" % str(cmd))
    print("param1: %s" % str(param1))

    try:
        client.request(cmd, param1)
    except Exception as e:
        success = "Failed: " + str(e)

    return success

def start():
    app.run()

if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt:
        print("Stopping webserver")
