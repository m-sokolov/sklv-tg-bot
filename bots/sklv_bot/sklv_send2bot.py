import requests
import configparser
import sys

# Load config file
config = configparser.ConfigParser()
config.read('../../config/main.ini')

# Load required parameters
BOT_TOKEN = config['SKLV_BOT']['BOT_TOKEN']
chat_id = config['SKLV_BOT']['sklv_chat_id']
server = config['GENERAL']['server']


def sendtobot(text):
    """Function will send passed information to tg"""
    requests.post(
        url='https://{0}/bot{1}/sendMessage'.format(server, BOT_TOKEN, ),
        data={'chat_id': chat_id,
              'text': text},
        verify=False
    ).json()


sendtobot(sys.argv[1])
