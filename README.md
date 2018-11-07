# SKLV's TG bot
Simple bot made just for fun. Web server handles all incoming requests and routes them to proper scripts/bots.

## Dependencies
For handling web requests I use Flask. Work with configuration files handled by Configparser.

### Adding new bot
To add new bot just:
* Ensure you registered bot on tg side
* Fill .ini file in config file new bot's information
* Add handle of new URL for your bot in Flask (web.py)
* Pass received json to your code
* ...
* Profit