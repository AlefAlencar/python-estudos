"""
DESAFIOS HACKERRANK

01. Arrays
"""


# Arrays-DS
'''def reverse_array(a):    # Write your code here
    return a[::-1]


arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))

print(' '.join(reverse_array(arr)))  # '''


# Dynamic Array
def dynamic_array(n, queries):
    last_answer = 0
    x, y = 1, 2
    answers_array = []
    for a in queries:
        if a[0] == 1:
            idx = (a[x] or last_answer) % n
            arr[idx].append(a[y])
        elif a[0] == 2:
            idx = (a[x] or last_answer) % n
            last_answer = arr[idx][a[y] % len(arr[idx])]
            answers_array.append(last_answer)
    return answers_array


n, q = list(map(int, input().split()))
queries = []

for _ in range(q):
    queries.append(
        list(map(int, input().split()))
    )

print(dynamic_array(n, queries))
