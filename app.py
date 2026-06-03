from http.server import HTTPServer,BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from CI/CD Pipline v1 , wuz up niggas!")

HTTPServer(("",8080), Handler).serve_forever()  