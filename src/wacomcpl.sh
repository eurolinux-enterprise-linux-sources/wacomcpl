#!/bin/sh
#
# Drop this into /etc/X11/xinit/xinitrc.d/

CONFIG_FILE=~/.wacomcplrc

if [ -f "$CONFIG_FILE" ]; then
    . "$CONFIG_FILE";
fi

