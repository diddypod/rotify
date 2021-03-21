#!/bin/python

import argparse
import json
import os
import requests
import subprocess
import sys
import yaml

parser = argparse.ArgumentParser(description='Check Gotify notifications')
parser.add_argument('-c', '--config', action='store', default='~/.config/rotify/config.yml',
                    help='specify a config file (default: ~/.config/rotify/config.yml)')
parser.add_argument('message', nargs='*', action='store',
                    help='message to be consumed')

args = parser.parse_args()

config_file = args.config
config = yaml.full_load(open(os.path.expanduser(config_file)))
gotify_url = config['gotify']['url']
client_token = config['gotify']['tokens']['client']

if (args.message):
    message = " ".join(args.message)
    try:
        subprocess.check_output(['xdg-open', message])
    except subprocess.CalledProcessError as e:
        p1 = subprocess.Popen(
            ['xclip', '-selection', 'clipboard', '-f'], stdin=subprocess.PIPE)
        p1.communicate(input=(message.encode()))
else:
    response = requests.get(
    '{0}/message?token={1}'.format(gotify_url, client_token))
    messages = json.loads(response.text)['messages']
    for message in messages:
        print(message['message'])
