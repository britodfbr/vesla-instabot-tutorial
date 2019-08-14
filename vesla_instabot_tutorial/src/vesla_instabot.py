import requests
import json
from .endpoints import endpoints

class VeslaInstaBot:
    def __init__(self):
        self.session = requests.Session()
        r = self.session.get(endpoints['base'])
        self.session.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
        self.user_id = None


    def login(self, credentials):
        r = self.session.post(endpoints['login'], data=credentials)
        self.session.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
        r = json.loads(r.content.decode('utf-8'))
        if r['authenticated']:
            self.user_id = r['userId']
        return r
