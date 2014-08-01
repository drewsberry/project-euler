fibonacci = [1, 2]

num_sum = 2

while True:

    fibonacci.append(fibonacci[-1] + fibonacci[-2])

    if fibonacci[-1] >= 4e6:
        break

    if not fibonacci[-1] % 2:
        num_sum += fibonacci[-1]

print "The sum of all of the even valued Fibonacci numbers below 4 million is "\
      "{sum}".format(sum=num_sum)
