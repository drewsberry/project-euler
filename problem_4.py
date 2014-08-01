def is_palindrome(x):

    if str(x) == str(x)[::-1]:
        return True

    return False

def find_palindromes(digits):
    # Find all palindromes which are products of two numbers with certain
    # number of digits

    palindromes = []

    min_num = 10 ** (digits - 1) + 1
    max_num = 10 ** (digits)
    
    for i in xrange(min_num, max_num):
        for j in xrange(min_num, max_num):
            if is_palindrome(i * j):
                palindromes.append(i * j)

    return palindromes

pals = find_palindromes(3)

print "The largest palindromic product of two 3-digit numbers is {pal}".format(
    pal=max(pals))
