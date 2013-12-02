#! /bin/sh
set -x
TRAPS="1 2 3 15"  # Signals and conditions to trap

function onexit {
  trap - $TRAPS
  echo "Terminating started processes "
  kill 0
}

#trap onexit HUP INT QUIT TERM # $TRAPS
trap onexit $TRAPS

#./t3.sh &
#echo t3 pid=$!
#wait

while true
do
 sleep 2
 echo "sleeping ... zzzzzz"
done

