"""
HACKERRANK
Algoritmhs:
1. Warm-up
"""


# 1/10 Solve Me First
'''def solveMeFirst(a,b):
    # Hint: Type return a+b below
    return a + b


num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1, num2)
print(res)  # '''

# 2/10 Simple Array Sum
'''def simpleArraySum(ar):
    # Write your code here
    return sum(ar)


ar_count = int(input().strip())
ar = list(map(int, input().rstrip().split()))
print(simpleArraySum(ar))  # '''

# 3/10 Compare the triplets
'''a = list(map(int, input().split()))
b = list(map(int, input().split()))
score_a = score_b = 0

for i in range(len(a)):
    score_a += a[i] > b[i]
    score_b += b[i] > a[i]

print(score_a, score_b  # '''


# 4/10 A very big sum
'''def sum_long_arr(ar):
    return sum(ar)


_, arr = input(), list(map(int, input().split()))
print(sum_long_arr(arr))  # '''


# 5/10 diagonal diference
'''def diagonal_difference(ar):
    primary_diagonal = sum(ar[i][i] for i in range(len(ar)))
    secondary_diagonal = sum(ar[i][-i-1] for i in range(len(ar)))
    # for i in range(len(ar)):
    #     secondary_diagonal += ar[i][-i-1]
    return abs(primary_diagonal - secondary_diagonal)


n = int(input().strip())  # tamanho da matriz
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
print(diagonal_difference(arr))  # '''

# 6/10 Plus Minus
'''# quantidade(positivos) / len(arr)
# quantidade(negativos) / "
# quantidade(zeros) / "

n, arr = int(input()), list(map(int, input().split()))
positives = negatives = zeros = 0
for i in arr:
    positives += i > 0
    negatives += i < 0
    zeros += i == 0
print(round(positives/n, 6))
print(round(negatives/n, 6))
print(round(zeros/n, 6))  # '''


# 7/10 staircase '#'
'''def staircase(n):    # Write your code here
    for i in range(1, n+1):
        print(f'{"#"*i:>{n}}')


n = int(input().strip())
staircase(n)  # '''


# 8/10 Min-Max Sum
'''def mini_max_sum(ar):
    arr_sums = []
    sum_arr = sum(ar)
    for i in range(len(ar)):
        arr_sums.append(sum_arr - ar[i])
    print(min(arr_sums), max(arr_sums))


arr = list(map(int, input().split()))
mini_max_sum(arr)  # '''


# 9/10 Birthday Cake Candles
'''def birthday_cake_candles(candles):
    return candles.count(max(candles))


candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))
print(birthday_cake_candles(candles))  # '''


# 10/10 Time Conversion
'''# 07:05:45PM -> 19:05:45
def timeConversion(s):    # Write your code here
    if s[-2:] == 'AM' and s[:2] == '12':
        return '00' + s[2:-2]
    elif s[-2:] == 'AM':
        return s[:-2]
    elif s[-2:] == "PM" and s[:2] == "12":
        return s[:-2]
    else:
        return str(int(s[:2]) + 12) + s[2:8]


s = input()
print(timeConversion(s))  # '''
