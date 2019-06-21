#!/usr/bin/python
from simple_websocket_server import WebSocketServer, WebSocket
import ssl

class SimpleEcho(WebSocket):
    def handle(self):
# echo message back to client
        self.send_message(self.data)

    def connected(self):
        print(self.address, 'connected')

    def handle_close(self):
        print(self.address, 'closed')

class SimpleChat(WebSocket):
    def handle(self):
        for client in clients:
            if client != self:
                client.send_message(self.data)

    def connected(self):
        print(self.address, 'connected')
        for client in clients:
            client.send_message(self.address[0] + u' - connected')
        clients.append(self)

    def handle_close(self):
        clients.remove(self)
        print(self.address, 'closed')
        for client in clients:
            client.send_message(self.address[0] + u' - disconnected')


clients = []


sslopts = dict(certfile="/home/romain/cert.pem", keyfile="/home/romain/key.pem", ssl_version=ssl.PROTOCOL_TLSv1);

server = WebSocketServer('172.25.28.5', 443, SimpleChat, **sslopts)
server.serve_forever()
