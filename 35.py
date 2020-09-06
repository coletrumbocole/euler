import math
import itertools

# Helpers
def answerCount(n):
  circularPrimes = []
  for x in range(2,n+1):
    if prime(x):
      primes.add(x)
  for p in primes:
    cycles = getRotations(p)
    # check each cycle is prime
    isCircular = True
    for c in cycles:
      if c not in primes:
        isCircular = False
    if isCircular:
      circularPrimes.append(p)
  return len(circularPrimes)

def prime(n):
  upperBound = int(math.sqrt(n))+1
  for x in range(2, upperBound):
    if n % x == 0:
      return False
  return True

def getRotations(n):
  # idea 1: slice the first [0:len] chars from the number, add to end. for a number 103, create ['1','0','3','1','0','3'] then grab [n:n+len] len times, 123, 231, 312
  s = str(n)
  scycles = s + s
  rotations = {n}
  for i in range(1,len(s)):
    rotations.add(int(scycles[i:i+len(s)]))
  return rotations
  # idea 2: keep looking for itertool to print each rotation for me. 

# Main
primes = set()
print(answerCount(1000000))
