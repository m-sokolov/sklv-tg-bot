#!/bin/bash
var=$(apt-get -u upgrade -s | grep "обновлено")
python3 sklv_send2bot.py "$var"
