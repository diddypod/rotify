#!/bin/python

import json
import os
import requests
import subprocess
import sys
import yaml

config_file = "~/.config/rotify/config.yml"
config = yaml.full_load(open(os.path.expanduser(config_file)))
gotify_url = config["gotify"]["url"]
client_token = config["gotify"]["tokens"]["client"]


def print_messages():
    response = requests.get(
        "{0}/message?token={1}".format(gotify_url, client_token))
    messages = json.loads(response.text)["messages"]
    for message in messages:
        print(message["message"])


if len(sys.argv) < 2:
    print_messages()
    exit()


message = sys.argv[1].encode()

try:
    subprocess.check_output(["xdg-open", message])
except subprocess.CalledProcessError as e:
    p1 = subprocess.Popen(
        ['xclip', '-selection', 'clipboard', '-f'], stdin=subprocess.PIPE)
    p1.communicate(input=(message))
