#! /bin/bash

set -x
trap 'echo "user says die ..."' SIGTERM
sleep 100
# Read characters from terminal one at a time.
echo -n "Enter a character: "
stty cbreak         # or  stty raw
readchar=`dd if=/dev/tty bs=1 count=1 2>/dev/null`
stty -cbreak
echo "Thank you for typing a $readchar ."

