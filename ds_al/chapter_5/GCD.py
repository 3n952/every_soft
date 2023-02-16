#greatest common divisor

'''euclidean algorithm'''

def gcd(x:int, y:int) -> int:
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

print(gcd(22, 8))
print(gcd(224,64))
print(gcd(64,224))