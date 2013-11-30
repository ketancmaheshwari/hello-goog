#! /bin/awk -f

#find mean and variance of a column from a file
BEGIN {
OFS=","
}
#body
{
$1=$1 #rebuild the record using current OFS
print $0
}
END {
print "Done" 
}
