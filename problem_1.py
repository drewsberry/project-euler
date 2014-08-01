num_sum = 0

for i in xrange(1,1000):
    if not i % 3 or not i % 5:
        num_sum += i

print "Sum of all numbers divisible by 3 or 5 is {sum}".format(sum=num_sum)
