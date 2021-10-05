"""
HACKERRANK preparação para entrevista

Core concepts:
01. WARM-UP CHALLENGES
"""

# 1/4 Sales by Match
'''import collections


def sockMerchant(n, ar):
    # Write your code here
    n = 0
    c = collections.Counter(ar)
    for k, v in c.items():
        n += v//2
    return n, c


n = int(input().strip())
ar = list(map(int, input().rstrip().split()))
print(sockMerchant(n, ar))  # '''

# 2/4 Counting Valleys
'''import itertools


def countingValleys(steps, path):
    grupos = []
    below_sea = False
    n = valleys = 0
    for key, values in itertools.groupby(path):
        if key == 'D':
            grupos.append(-len(list(values)))
        else:
            grupos.append(len(list(values)))
    for v in grupos:
        n += v
        print(n)
        if n < 0 and below_sea is False:
            below_sea = True
            valleys += 1
        if n >= 0 and below_sea is True:
            below_sea = False
    return grupos, valleys


steps = int(input().strip())
path = input()
print(countingValleys(steps, path))  # '''


# 3/4 Jumping on the Clouds
'''def jumpingonclouds(c):
    # c = mj = 0  # minimum jumps
    # s = len(clouds)
    # while c < s-1:
    #     try:
    #         if not clouds[c+2]:
    #             c += 2
    #         elif not clouds[c+1]:
    #             c += 1
    #         mj += 1
    #     except:
    #         pass
    # return mj
    j = x = 0
    while x < len(c)-1:
        print(x)
        try:
            if c[x+2] == 0:
                x += 1
        except IndexError:
            pass
        x += 1
        j += 1
    print(x)
    return j


n = int(input().strip())
c = list(map(int, input().split()))
print('return', jumpingonclouds(c))  # '''


# 4/4 Repeated String
def repeated_string(s, n):  # s=aba, n=11
    # subtring: 'aba aba aba ab'  --> (2+2) +1 = 5 a's
    x = n//len(s)
    a = s.count('a')
    p = s[:n%len(s)].count('a')
    res = (x * a) + p
    print(x, a, p)
    return res


s = input()
n = int(input())
print(repeated_string(s, n))  # '''
