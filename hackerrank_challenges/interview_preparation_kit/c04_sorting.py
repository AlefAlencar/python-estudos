"""
HACKERRANK preparação para entrevista
04. Sorting
"""


# Sorting: Bubble Sort
'''def count_swaps(a):
    c = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                x = a[j+1]
                a[j+1] = a[j]
                a[j] = x

                c += 1
    print(c, '\n', a)


n = int(input().strip())
a = list(map(int, input().rstrip().split()))
count_swaps(a)  # '''


# Mark and Toys
def maximum_toys(prices, k):
    prices.sort()
    i = c = 0
    for p in prices:
        if i + p > k:
            break
        i += p
        c += 1
    return c


n, k = list(map(int, input().rstrip().split()))
prices = list(map(int, input().rstrip().split()))
print(maximum_toys(prices, k))  # '''

#