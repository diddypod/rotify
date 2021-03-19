#!/bin/python

import os
import requests
import sys
import yaml

if len(sys.argv) < 2:
    exit()

config_file = "~/.config/rotify/config.yml"
config = yaml.full_load(open(os.path.expanduser(config_file)))
gotify_url = config["gotify"]["url"]
app_token = config["gotify"]["tokens"]["app"]
title = config["sender"]["title"]
priority = config["sender"]["priority"]

payload = {
    "title": title,
    "priority": priority,
    "message": sys.argv[1:]
}

requests.post("{0}/message?token={1}".format(gotify_url, app_token), payload)
