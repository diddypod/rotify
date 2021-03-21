#!/bin/python

import argparse
import os
import requests
import sys
import yaml

parser = argparse.ArgumentParser(description='Send notifications via Gotify')
parser.add_argument('message', type=str, nargs='*',
                    help='Message to send to Gotify')
parser.add_argument('-c', '--config', action='store', default='~/.config/rotify/config.yml',
                    help='specify a config file (default: ~/.config/rotify/config.yml)')

args = parser.parse_args()

config_file = args.config
config = yaml.full_load(open(os.path.expanduser(config_file)))
gotify_url = config['gotify']['url']
app_token = config['gotify']['tokens']['app']
title = config['sender']['title']
priority = config['sender']['priority']

payload = {
    'title': title,
    'priority': priority,
    'message': " ".join(args.message)
}

requests.post('{0}/message?token={1}'.format(gotify_url, app_token), payload)
