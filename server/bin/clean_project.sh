#!/bin/sh

sh stop_server.sh

pidfile="../proc/pid"

if [ -e $pidfile ]; then
  rm $pidfile
fi

rm ../log/*.log*
rm ../src/gameserver/*.pyc

