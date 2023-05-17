import http.server
import socketserver

# Specify the host and port to listen on
host = "0.0.0.0"  # Listen on all available network interfaces
port = 8000  # Example port, you can choose any available port

# Create a custom request handler
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hello, World!</h1>")

# Create the server
server = socketserver.TCPServer((host, port), MyRequestHandler)

# Start the server
print(f"Server listening on {host}:{port}")
server.serve_forever()
