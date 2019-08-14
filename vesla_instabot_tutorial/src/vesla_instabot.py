import requests
from .endpoints import endpoints

class VeslaInstaBot:
    def __init__(self):
        self.session = requests.Session()
        r = self.session.get(endpoints['base'])
        self.session.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
        self.user_id = None
