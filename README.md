# rotify

## Description
Send and view [Gotify](https://gotify.net) messages

## Features
### notify
- Send notifications
- Configure priority

### checknotifs
- List notifications
- Use `xdg-open` to open in relvant application, else copy to clipboard using `xclip`

## Screenshots
### Send notifications
<img src=./screenshots/notify.png width=800px>

### Check notifications
<img src=./screenshots/checknotifs.png width=800px>

## Installation
### Depenencies
 - python3
 - xsel (to use rotify.sh -i)
 - xdg-open (to open in applications from checknotifs with rofi)
 - xclip (to copy to clipboard from checknotifs with rofi)

Clone this repository and copy `config.yml` to `~/.config/rotify/config.yml`
```
git clone https://github.com/diddypod/rotify
cp ./rotify/config.yml ~/.config/rotify/config.yml
```
Edit `~/.config/rotify/config.yml`

## Usage
### With rofi
```
rofi -show notify -modi notify:.../rotify/notify.py                 #Send notification

rofi -show checknotifs -modi checknotifs:.../rotify/checknotifs.py  #Check notifications
```
### notify
```
usage: notify.py [-h] [-c CONFIG] [message ...]

Send notifications via Gotify

positional arguments:
  message               Message to send to Gotify

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        specify a config file (default: ~/.config/rotify/config.yml)
```
### checknotifs
```
usage: checknotifs.py [-h] [-c CONFIG] [message ...]

Check Gotify notifications

positional arguments:
  message               message to be consumed

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        specify a config file (default: ~/.config/rotify/config.yml)
```
There's also a handy wrapper, `rotify.sh`, which you can use to call checknotifs and notify, the latter with or without rofi (without rofi, it gets the current selection using xsel and sends it to Gotify)
```
rotify - send/read Gotify notifications
 
rotify [options]
 
options:
-c        config path [default ~/.config/rotify/config.yml]
-s        send notification via rofi
-r        read notifications via rofi
-i        send selected text without rofi
-h        show this help
```

## Windows

If you feel like you have an appetite for fairly disappointing results and a not particularly "nice" experience, but you agree that something is better than nothing, you can get these scripts running in Windows. I'll touch on it briefly.

I'm using [Powertoys Run](https://docs.microsoft.com/en-gb/windows/powertoys/run#features) as a launcher, which can run shell scripts.

- Enable the scripts toggle in Powertoys Run
- Clone scripts, add them to PATH and reboot (PToys Run uses the Windows indexer and rebooting is the easiest way to make sure the indexes are up to date)
- Update the script shebangs to `#!python` to get them working on Windows, point them to the new config path
- Remove all the nice `xdg-open` and `xclip` stuff from `checknotifs.py`, since that won't work on Windows and make sure it waits for user input before exiting, the script runs outside the launcher in a termimnal window
- Open PToys Run with the hotkey and type in `>notify.py message` to send a notification, `>checknotifs.py` to list them
