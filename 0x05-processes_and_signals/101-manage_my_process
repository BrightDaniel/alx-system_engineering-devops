#!/usr/bin/env bash
# Manages 'manage_my_process'

if [ "${1}" == "start" ]
then
    ./manage_my_process &
    touch /var/run/my_process.pid
    echo "$!" > /var/run/my_process.pid
    echo "manage_my_process started"
elif [ "${1}" == "stop" ]
then
    echo "manage_my_process stopped"
    kill "$(cat /var/run/my_process.pid)"
    rm /var/run/my_process.pid
elif [ "${1}" == "restart" ]
then
    kill "$(cat /var/run/my_process.pid)"
    rm /var/run/my_process.pid
    ./manage_my_process &
    touch /var/run/my_process.pid
    echo "$!" > /var/run/my_process.pid
    echo "manage_my_process restarted"
else
    echo "Usage: manage_my_process {start|stop|restart}"
fi
