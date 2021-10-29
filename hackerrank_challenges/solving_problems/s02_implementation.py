"""
DESAFIOS HACKERRANK
Solving Problems
Algorithms:
2. Implementation

66 problems to solve
"""


# 1 Grading Students
'''def grading_students(gr):
    for i in range(len(gr)):
        if gr[i] % 5 > 2 and gr[i] >= 38:
            gr[i] = gr[i] - (gr[i] % 5) + 5
    return gr


grades_count = int(input().strip())
grades = []
for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)
print(grading_students(grades))  # '''


# 2 Apple and Orange
'''def count_apples_and_oranges(s, t, a, b, apples, oranges):
    # area: s, t
    # trees: apple = a, orange = b
    # arrays: distances that fruits falls from the trees
    apples_position = [distance + a for distance in apples]
    oranges_position = [distance + b for distance in oranges]
    fruits_in = [
        str(sum([s <= fruit <= t for fruit in apples_position])),
        str(sum([s <= fruit <= t for fruit in oranges_position])),
    ]
    for i in fruits_in:
        print(i)


first_multiple_input = input().rstrip().split()  # Sam's house
s = int(first_multiple_input[0])
t = int(first_multiple_input[1])
second_multiple_input = input().rstrip().split()  # trees positions
a = int(second_multiple_input[0])
b = int(second_multiple_input[1])
third_multiple_input = input().rstrip().split()  # number of fruits
m = int(third_multiple_input[0])
n = int(third_multiple_input[1])
apples = list(map(int, input().rstrip().split()))  # distances from apple tree
oranges = list(map(int, input().rstrip().split()))  # distances from orange tree
count_apples_and_oranges(s, t, a, b, apples, oranges)  # '''


# 3 Number Line Jumps  {1ª: 8/30fail 7.84pts; 2ª: 0/30 +10pts}
'''def kangaroo(x1, v1, x2, v2):  # 0 3 4 2 = Y; 0 2 5 3 = N
    if v1 <= v2:  # ve se eh menor ou igual, pois jamais alcancarah
        return 'NO'
    else:
        while x1 < x2:  # se o primeiro canguru ainda estah atras
            x1 += v1  # pule
            x2 += v2
        else:  # eh igual ou maior
            if x1 == x2:
                return 'YES'
            else:
                return 'NO'


first_multiple_input = input().rstrip().split()
x1 = int(first_multiple_input[0])
v1 = int(first_multiple_input[1])
x2 = int(first_multiple_input[2])
v2 = int(first_multiple_input[3])
print(kangaroo(x1, v1, x2, v2))  # '''


# 4 Between Two Sets  {1º 1/9failed 8.57/10pts;}
# 1. descobrir os múltiplos comuns que estão entre as matrizes
# 2. descobrir quais dos múltiplos comuns são comuns a segunda matriz
# 3. retornar quantos são esses múltiplos
'''from math import lcm, gcd
def getTotalX(a, b):
    x = lcm(*a)
    y = gcd(*b)
    n = 0
    for i in range(x, y+1):
        n += y % i == 0
    return x, y, n


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
arr = list(map(int, input().rstrip().split()))
brr = list(map(int, input().rstrip().split()))
print(getTotalX(arr, brr))  # '''


# 5 Breaking the Records
'''def breaking_records(scores):    # Write your code here
    best_score = worst_score = scores[0]  # primeiro valor
    brokes_best = brokes_worst = 0  # numeros de recordes quebrados, melhor e pior
    for score in scores:
        if score > best_score:
            best_score = score
            brokes_best += 1
        elif score < worst_score:
            worst_score = score
            brokes_worst += 1
    return brokes_worst, brokes_best


n = int(input().strip())
scores = list(map(int, input().rstrip().split()))
print(breaking_records(scores))  # '''


# 6 Subarry Division
'''# n squares
# s[i], the numbers in chocolate squares
# d result of the sum, m lenght of segments to sum
def birthday(s, d, m):    # Write your code here
    res = [1 for i in range(0, len(s)) if sum(s[i:i+2]) == d]
    return sum(res)


n = int(input().strip())
s = list(map(int, input().rstrip().split()))
first_multiple_input = input().rstrip().split()
d = int(first_multiple_input[0])
m = int(first_multiple_input[1])
print(birthday(s, d, m))  # '''


# 7 Divisible Sum Pairs
'''def divisible_sum_pairs(n, k, ar):    # Write your code here
    res = []
    for i in range(len(ar)):
        for j in range(i+1, len(ar)):
            print(ar[i], '+', ar[j], '=', ar[i] + ar[j], '/', k, '=', (ar[i] + ar[j])/k)
            res.append((ar[i]+ar[j]) % k == 0)
    return sum(res)


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
ar = list(map(int, input().rstrip().split()))
print(divisible_sum_pairs(n, k, ar))  # '''


# 8 Migratory Birds  {1ª 1/6failed, 7.5/10pts; 2ª OK}
'''import collections
def migratory_birds(arr):    # Write your code here
    # c = [(k, v) for k, v in collections.Counter(arr).items()]
    # return max(c, key=lambda x: x[1])[0]
    x = [
        (1, arr.count(1)),
        (2, arr.count(2)),
        (3, arr.count(3)),
        (4, arr.count(4)),
        (5, arr.count(5)),
    ]
    return max(x, key=lambda i: i[1])[0]
# 11
# 1 2 3 4 5 4 3 2 1 3 4
# Counter({3: 3, 4: 3, 1: 2, 2: 2, 5: 1})


arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
print(migratory_birds(arr))  # '''


# 9 Day of the Programmer {1ª 10/61failed 12/15pts; }
def day_of_programmer(year):    # Write your code here
    if year < 1918:
        return f'12.09.{year}'
    elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return f'12.09.{year}'
    else:
        return f'13.09.{year}'


year = int(input().strip())
print(day_of_programmer(year))  # '''


# 10 Electronics Shop
'''def get_money_spent(keyboards, drives, b):    # Write your code here.
    ms = 0
    for k in keyboards:
        for d in drives:
            x = k + d
            if b >= x > ms:
                ms = x
    if ms == 0:
        return -1
    else:
        return ms


b, n, m = input().split()
keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))

print(get_money_spent(keyboards, drives, b))  # '''


# 11