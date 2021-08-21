import requests
import datetime

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


bot_token = "1917504592:AAEamp3mDUwMrimPMek_96ho3UFMyEIZ8_c"
greet_bot = BotHandler(bot_token)
greetings = ('hello', 'hi', 'greetings', 'sup')  
now = datetime.datetime.now()
 
def main():
    new_offset = None
    today = now.day
    hour = now.hour
    while True:
        greet_bot.get_updates(new_offset)
        last_update = greet_bot.get_last_update()
        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']
        
        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Good Morning  {}'.format(last_chat_name))
            today += 1
        
        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Good Afternoon {}'.format(last_chat_name))
            today += 1
        
        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Good Evening  {}'.format(last_chat_name))
            today += 1
        
        new_offset = last_update_id + 1

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()