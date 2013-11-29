#! /bin/awk -f

#find mean and variance of a column from a file
BEGIN {
print "Hello Regular Expressions"
command = sprintf("sleep %d", 2)
system (command) #way cool, execute system command
}
#body
/^1/{
print
lin=lin+1
}
END { 
print lin
}
