#!/bin/env python

#mainly for sys.argv[], sys.argv[0] is the name of the program
import os
import optparse

p=optparse.OptionParser()

p.add_option("-t", action="store_true", dest="tracing")

p.add_option("-o", "--outfile", action="store", type="string", dest="outfile")

p.add_option("-d", "--debuglevel", action="store", type="int", dest="debug")

p.add_option("--speed", action="store", type="choice", dest="speed", choices=["slow", "fast", "ludicrous"])

p.add_option("--coord", action="store", type="int", dest="coord", nargs=2)

p.set_defaults(tracing=False,
               debug=0,
               speed="fast",
               coord=(0,0),
               mode="novice")

opt, args = p.parse_args()

print "tracing :", opt.tracing
print "outfile :", opt.outfile
print "debug :", opt.debug
print "speed :", opt.speed
print "coord :", opt.coord
print "mode :", opt.mode

