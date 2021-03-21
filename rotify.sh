#!/bin/sh

package="rotify"

config="~/.config/rotify/config.yml"
immediate=0
sender=0

print_help() {
    echo "$package - send/read Gotify notifications"
    echo " "
    echo "$package [options]"
    echo " "
    echo "options:"
    echo "-c        config path [default ~/.config/rotify/config.yml]"
    echo "-s        send notification via rofi"
    echo "-r        read notifications via rofi"
    echo "-i        send selected text without rofi"
    echo "-h        show this help"
    exit 1
}

if test $# -eq 0;
then
    print_help
fi

while getopts 'c:srih' OPTION; do
    case "$OPTION" in
        c)
            config=$OPTARG;
        ;;
        s)
            sender=1;
        ;;
        r)
            sender=0;
        ;;
        i)
            immediate=1;
        ;;
        ?)
    	    print_help
        ;;
    esac
done

shift "$(($OPTIND -1))"

if [ $immediate -eq 1 ]; then
    message="`xsel`"
    exec ~/scripts/notify -c "$config" "$message"
fi

if [ $sender -eq 1 ]; then
    exec rofi -show notify -modi notify:~/scripts/notify -c "$config"
else
    exec rofi -show check-notifs -modi check-notifs:~/scripts/checknotifs
fi