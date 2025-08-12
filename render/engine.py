from typing import Callable, Literal
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleServer(BaseHTTPRequestHandler):
    ...
    
    

def route(path: str, method: Literal["GET", "POST", "PUT", "DELETE"] = None):
    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            server = HTTPServer(('localhost', 8000), SimpleServer)
            
            if method == "GET":
                
                def f(self):
                    if self.path == path:
                        self.send_response(200)
                        self.send_header("Content-type", "text/html")
                        self.end_headers()
                        self.wfile.write(result.encode('utf-8'))
                        
                setattr(SimpleServer, "do_GET", f)
            
            server.serve_forever()
            
            return result
        return wrapper 
    return decorator
        