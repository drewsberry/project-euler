from __future__ import division

import itertools

answer = 232792560

for i in itertools.count(21):

    if (i / answer)*100*1000 % 1 == 0:
        print i / answer, " thousands of a %"
    

    res = True
    
    for divisor in xrange(1, 21):
        if i % divisor != 0:
            res = False
            break

    if res == True:
        print i
        raise Exception
    else:
        continue

print i

# This technically functions, but it takes forever
