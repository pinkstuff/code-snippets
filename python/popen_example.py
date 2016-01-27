#! /usr/bin/python

from subprocess import PIPE, Popen
import os


# by making kwargs stderr, stdin and stdout = None this prints stuff to the screen
# which may not be what we want.
# Some developers like to open a file object pointing to /dev/null (or os.devnull) so they send
# the output down a blackhole

devnull_in = open(os.devnull, 'w')
devnull_out = open(os.devnull, 'r')



# Duncan warns about leaving shell=True becuase of shell injection, 
# like nasty things in backquote and "; rm -rf / >/dev/null 2>&1 &"

sesh = Popen(['ls', '-a', '-l', '~'], shell=False,
             stdin=devnull_out, stderr=devnull_in, stdout=PIPE)

for line in sesh.stdout:
    print ">>>>\t%s" % line.strip()

