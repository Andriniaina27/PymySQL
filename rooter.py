import re
class Route(object):
    def __init__(self, path, handler):
        self.path    = re.compile(path)
        self.handler = handler
    
class Router(object):
    def __init__(self):
        self.routes = []
    
    def add(self, path, handler):
        self.routes.append(Route(path, handler))
    
    def resolve(self, path):
        for route in self.routes:
            if route.path.fullmatch(path):
                return route.handler
        return None