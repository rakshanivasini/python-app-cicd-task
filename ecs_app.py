from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        try:
            # Read the binary data from the GIF file
            with open('welcome.gif', 'rb') as file:
                gif_data = file.read()

            # Write the binary data to the response
            self.wfile.write(gif_data)
            #self.wfile.write(b'Hi, I am a python app executing from ECS')
        except FileNotFoundError:
            self.wfile.write(b'Error while reading the file')# Handle the case where the GIF file isn't found
            self.wfile.write(b'gifpath',gif_data) 
            self.send_error(404, 'File Not Found: %s' % gif_path)
        except Exception as e:
            self.wfile.write(b'Unknown error: %s' % e) 
        

server = HTTPServer(('0.0.0.0', 8000), SimpleHandler)
server.serve_forever()
