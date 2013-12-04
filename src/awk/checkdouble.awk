#! /bin/awk -f

#check back to back double occurrence of a word

BEGIN {
}

#body
FILENAME != prevfile {
  NR = 1
  prevfile = FILENAME
}
NF > 0{
  if ($1 == lastword && $1 != "had")
     printf "double %s, file %s, line %d\n", $1, FILENAME, NR
  for (i=2; i <= NF; i++)
      if ($i == $(i-1) && $i != "had")
         printf "double %s, file %s, line %d\n", $i, FILENAME, NR
  if (NF > 0){
     lastword = $NF
  }
}
END { 
}
