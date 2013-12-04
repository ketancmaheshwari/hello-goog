#!/bin/bash

NUM_YRS=$1
ALINE="grid_ID,"

#concatenate string grid_ID with commas
for i in `seq 1 $NUM_YRS`
do
  ALINE=$ALINE$i","
done

#remove the last comma from the header line
HLINE=`echo $ALINE | sed 's/,$//'`

for i in `find summaries/ -type f -iname *.OUT`
do
bname=`basename $i Summary.OUT`
#echo $bname
awk -v numyrs=$NUM_YRS -v prepend=$bname '
BEGIN{
offset=4
}

NR>offset&&NR<=offset+numyrs{
 str1=str1","$21
}

NR>offset+numyrs&&NR<=offset+numyrs*2{
 str2=str2","$21
}

NR>offset+numyrs*2&&NR<=offset+numyrs*3{
 str3=str3","$21
}

NR>offset+numyrs*3&&NR<=offset+numyrs*4{
 str4=str4","$21
}

NR>offset+numyrs*4&&NR<=offset+numyrs*5{
 str5=str5","$21
}

NR>offset+numyrs*5&&NR<=offset+numyrs*6{
 str6=str6","$21
}

NR>offset+numyrs*6&&NR<=offset+numyrs*7{
 str7=str7","$21
}

NR>offset+numyrs*7&&NR<=offset+numyrs*8{
 str8=str8","$21
}

END{
print prepend","str1 >> "H1_1.csv"
print prepend","str2 >> "H1_2.csv"
print prepend","str3 >> "H1_3.csv"
print prepend","str4 >> "H1_4.csv"
print prepend","str5 >> "H1_5.csv"
print prepend","str6 >> "H1_6.csv"
print prepend","str7 >> "H1_7.csv"
print prepend","str8 >> "H1_8.csv"
}
' $i
done

for i in `/bin/ls -1 *.csv`
do
 #remove double commas
 sed -i 's/,//' $i
 #insert hline as header
 sed -i "1 i $HLINE" $i
 #remove blank lines (ie. lines which do not have a comma)
 sed -i -n -e '/,/p' $i
done

