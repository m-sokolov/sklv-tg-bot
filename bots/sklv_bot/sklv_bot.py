import subprocess
import configparser
import sys
import json
import os
import requests

# As this code is called from Flask, you may want to change working directory to current one
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Load config file
config = configparser.ConfigParser()
config.read('../../config/main.ini')

# Load token, chat id and proxy server
BOT_TOKEN = config['SKLV_BOT']['BOT_TOKEN']
chat_id = config['SKLV_BOT']['sklv_chat_id']
server = config['GENERAL']['server']


def get_serv_updates():
    """Function will call script that gathers information about updates"""
    process = subprocess.Popen(['./upgrade_row.sh'], stdout=subprocess.PIPE)
    process.communicate()


def random_wiki(chat):
    """Function will get and return random page from Wiki"""
    response = requests.get(
        'https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:'
        + '%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
    )
    sendtobot(chat, response.url)


def sendtobot(chat, text_to_send):
    """Function sends passed information to tg"""
    requests.post(
        url='https://{0}/bot{1}/sendMessage'.format(server, BOT_TOKEN, ),
        data={'chat_id': chat,
              'text': text_to_send},
        verify=False  # I trust my self-signed certificated on proxy server
    ).json()


# Available bot functions
commands = {'updates': get_serv_updates,
            'random_wiki': random_wiki}

# Convert passed string from Flask to json object with load function
json = json.loads(sys.argv[1])
print(json)
msg = json['message']
txt = json['message']['text']
chat = json['message']['chat']['id']
try:
    # Text from chat comes as /command@botname split this row and delete first symbol
    command = txt.split('@')
    if commands[command[0][1:]]:
        commands[command[0][1:]](chat)
    else:
        print("No such command")
except Exception as e:
    print(e)
