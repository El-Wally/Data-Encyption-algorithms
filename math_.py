def squareMultiply (b, p, n): # base, power
    # x^0 = 1
    if p == 0:
        return 1 % n

    # x^1 = x
    if p == 1:
        return b % n

    # if p is odd
    if p%2 == 1:
      return ( b * squareMultiply(b*b, (p-1)//2, n ) ) % n
    else: # p is even
        return ( squareMultiply(b*b, p//2, n) ) % n


# Euclidean GCD
def eucGCD(a, b):
    if b == 0:
        return a
    else:
        return eucGCD(b, a%b)

# Extended Euclidean Algorithm, a(s)+b(t) form
def extEucAlg(a, b):
    # if b divides a, then clearly it is the gcd
    if a%b == 0:
        return (b, 0, 1)
    else:
        gcd, s, t = extEucAlg(b, a%b)
        s = s - ( (a//b) * t) # (a//b)t here is the b(t) of previous iteration
        return (gcd, t, s)
 
# Multiplicative Inverse
def mulInv(a, b):
    gcd, s, t = extEucAlg(a, b)
    return s%b