import requests

class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        params = {'timeout': timeout, 'offset': offset}
        method = 'getUpdates'
        response = requests.get(self.api_url + method, params)
        return response.json()['result']

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        response = requests.post(self.api_url + method, params)
        return response

    def get_last_update(self):
        result = self.get_updates()
        last_update = result[len(result)-1]
        return last_update

    def first_update(self):
        result = self.get_updates()
        if len(result) == 0:
            return None
        return result[0]

    def get_chat_id(update):
        return update['message']['chat']['id']
