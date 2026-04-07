import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 5000))
HOST = "0.0.0.0"

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "":
            self.path = "/index.html"
        return super().do_GET()

    def log_message(self, format, *args):
        print(f"[{self.address_string()}] {format % args}", flush=True)

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "public"))

with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    httpd.allow_reuse_address = True
    print(f"Serving on http://{HOST}:{PORT}", flush=True)
    httpd.serve_forever()
