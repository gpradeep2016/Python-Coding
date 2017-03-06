'Quick whirlwind tour of highlights of the standard library'

import collections

pref = collections.OrderedDict()
pref['raymond'] = 'red'
pref['rachel'] = 'blue'
pref['matthew'] = 'yellow'
print pref

colors = 'red green red blue green red'.split()
counts = collections.Counter()
for color in colors:
    counts[color] += 1
print counts

from bisect import bisect

test_scores = [55, 87, 61, 90, 72, 98, 84]
grades = ['F', 'D', 'C', 'B', 'A']
cuts = [60, 70, 80, 90]
for score in test_scores:
    grade = grades[bisect(cuts, score)]
    print score, '-->', grade

import glob                          # Expand glob wildcards

print glob.glob('*.py')

import shutil                        # Tools for manipulating files

shutil.copyfile('analysis.py', 'analysis.tmp')
shutil.move('analysis.tmp', 'analysis.bak')

import os                            # Interface with the operating system

print os.system('dir /w > tmp.txt')        # Let's you run ANY command sequence from Python
os.remove('tmp.txt')                 # Deletes files

import subprocess                    # Utilities for running other programs
                                     # and controlling the inputs, outputs, error outputs
                                     # and process management (waiting, suspending, killing)

s = subprocess.check_output('netstat -a', shell=True)  # Runs a command, waits for it, captures its output
print s[:500]

s = subprocess.check_output(['netstat', '-a'])         # Faster than the shell version, but you lose all shell capabilities
print s[:500]

