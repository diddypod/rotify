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
Clone this repository and copy `config.yml` to `~/.config/rotify/config.yml`.
```
git clone https://github.com/diddypod/rotify
cp ./rotify/config.yml ~/.config/rotify/config.yml
```
Edit `~/.config/rotify/config.yml`.

## Usage 
```
rofi -show checknotifs -modi checknotifs:.../rotify/checknotifs.py #Check notifications

rofi -show notify -modi checknotifs:.../rotify/notify.py #Send notification
```