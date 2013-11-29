#! /bin/awk -f

#find mean and variance of a column from a file
BEGIN {
print "Hello awk"
}

#body
{
sum = sum + $4
}
END { 
print NR
print sum 
mean = sum / NR
print mean
}
