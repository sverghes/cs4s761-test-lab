from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class PingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        msg = f"Pong from node: {socket.gethostname()}\n"
        self.wfile.write(msg.encode())

HTTPServer(("0.0.0.0", 5000), PingHandler).serve_forever()
