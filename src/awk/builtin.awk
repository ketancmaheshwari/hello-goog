#! /bin/awk -f

#find mean and variance of a column from a file
BEGIN {
}
#body
{
   alen=length($2)
   if (alen >= 29)
      print $2, alen
}
END { 
}
