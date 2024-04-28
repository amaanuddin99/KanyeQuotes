import requests
class Quote:
    def __init__(self):
        response=requests.get(url="https://api.kanye.rest")
        self.newq=response.json()

