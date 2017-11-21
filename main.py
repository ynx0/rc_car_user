import hardware_server
import webserver
#from drivers import keyboard_cli

print("Starting up servers")

hardware_server.start()
# keyboard_cli.start()
webserver.start()


