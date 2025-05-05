from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, World from Docker! This is a simple demonstration of how basic Docker applications work.")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), HelloHandler)
    print("Starting server on port 8080...")
    server.serve_forever()
