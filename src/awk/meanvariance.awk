#! /bin/awk -f

#find mean and variance of a column from a file
BEGIN {
print "Hello awk"
}

#body
{
sum = sum + $4
sum2 = sum2 + $4*$4
}
END { 
print NR
print sum 
mean = sum / NR
variance = ((sum * sum) - sum2) / NR
print mean
print variance
stdev=sqrt(variance)
print stdev
}
