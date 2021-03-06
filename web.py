import os
import json
import configparser
import re
from flask import Flask, request, redirect

# Load config file
config = configparser.ConfigParser()
config.read('config/main.ini')
ip = config['GENERAL']['local_ip']
port = config['GENERAL']['local_port']

app = Flask(__name__)

# Delimiters for command splitting
delim = re.compile("[/@\s]")

# Next row will define URL and method
@app.route("/api/sklv_bot", methods=['POST'])
def sklv_bot():
    """Pass received json to bot, dump function will convert json to string"""

    # Get json with all "command:file" values
    with open("bots.json", "r") as f:
        bots = json.load(f)
        f.close()

        # Get command from request
        txt = request.json['message']['text']
        command = re.split(delim, txt)

        # Launch file if exists
        if command[1] in bots:
            os.system("python3 {} '{}'".format(bots.get(command[1]), json.dumps(request.json)))

    # Please return code 200 to tg, to prevent multiply send
    return "ok", 200


# Catch all incorrect url calls
@app.errorhandler(404)
def page_not_found():
    return redirect("http://lurkmore.to/%D0%9A%D1%82%D0%BE_%D0%B2%D1%8B_%D1%82%D0%B0%D0%BA%D0%B8%D0%B5%3F_%"
                    + "D0%AF_%D0%B2%D0%B0%D1%81_%D0%BD%D0%B5_%D0%B7%D0%BD%D0%B0%D1%8E", 302)


# Define Flask start parameters server and port. I prefer to keep certificates in ssl folder
if __name__ == "__main__":
    app.run(host=ip,
            port=port,
            ssl_context=('ssl/cert.pem',
                         'ssl/key2.pem'))
