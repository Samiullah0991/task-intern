from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from link_finder import find_links  # Importing the find_links function from link_finder.py

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve index.html on GET request to root URL
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

    def do_POST(self):
        # Parse POST request to extract URL from form submission
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        url = parse_qs(post_data)['url'][0]

        # Call find_links function to get links data
        links_data = find_links(url)

        # Send response with links data
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(links_data.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=5500):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
