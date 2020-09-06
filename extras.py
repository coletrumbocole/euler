# extra stuff
# will I run out of recursion?
# how many primes in 1 - 1,000,000? 78499
# Yes. 1000 < 78499

def printUseful(n):
  upperBound = int(math.sqrt(n))+1
  for x in primes:
    if x <= upperBound:
      print(x)

def primeSlow(n, primes): # Because of Copying?
  upperBound = int(math.sqrt(n))+1
  if n == upperBound:
    primes.append(n) # is this doing what I think it does? yes, mutates global primes
    return True
  useful = [x for x in primes if x <= upperBound]
  for x in useful: # I just want to optimize here, this range, should only use primes.
    if n % x == 0:
      return False
  primes.append(n)
  return True

def answer(n):
  for x in range(2,n+1): # it is not inclusive of the last numbe, that's why I had +1 earlier.
    a = "Is "
    a += str(x)
    a += " prime? "
    if prime(x): # I wonder why people push for code reusability? If 10 other parts of my program use this function, and I change it, now 10 places are broken instead of just this one. What design pattern will help me avoid this?
      a += "yes"
    print(a)

# answer(1000000)
# printUseful(17) # remember to set primes accordingly, since there is no append within this function.
