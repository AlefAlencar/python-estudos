"""
HACKERRANK preparação para entrevista

03. DICTIONARIES AND HASHMAPS
"""


# 1/5 Hash Tables: Ransom Note
'''def check_magazine(m, n):
    for w in n:
        print(w)
        try:
            print(m.remove(w))
        except ValueError:
            return print('No')
        finally:
            print(m)
    return print('Yes')


a, b = input().split()
magazine = input().split()
note = input().split()
check_magazine(magazine, note)  # '''


# 2/5 Two Strings  {1ªtent: 4/8failed 5pts; 2ª: 3/8f 10p; 3ª: 0/15 25pts}
'''# *** timeout ***
def two_strings(s1, s2):
    # ss1 = gen_substrs(s1)
    # ss2 = gen_substrs(s2)
    # print(ss1)
    # print(ss2)
    # for s in ss1:
    #     if s in ss2:
    #         return 'Yes'
    # return 'No'
    # if len(s1) > len(s2):
    #     temp = s1
    #     s1 = s2
    #     s2 = temp
    # i = 0  # initial
    # while i < len(s1):
    #     e = len(s1)  # end
    #     while i != e:
    #         #print(s1[i:e])
    #         if s1[i:e] in s2:
    #             return 'YES'
    #         e -= 1
    #     i += 1
    # return 'NO'
    # muito muito muito mais simples:
    return 'YES' if set(s1) & set(s2) else 'NO'


def gen_substrs(s1):
    i = 0
    substrings = []
    while i < len(s1):
        j = len(s1)
        while j != i:
            substrings.append(s1[i:j])
            j -= 1
        i += 1
    return substrings


for _ in range(int(input())):
    str1 = input()
    str2 = input()
    print(two_strings(str1, str2))  # '''


# 3/5 Sherlock and Anagrams (medium)
import itertools


def sherlock_and_anagrams(s):
    s = list(s)
    lss = {}
    i = 0
    while i < len(s):
        j = len(s)
        while i != j:
            ss = sorted(s[i:j])
            ss = ''.join(ss)
            print(ss)
            if ss in lss:
                lss[ss] += 1
            else:
                lss[ss] = 1
            j -= 1
        i += 1

    c = 0
    for k, v in lss.items():
        print(k, ':', v)
        c += v//2
    print()
    print(c, lss)
    return


for _ in range(int(input())):
    st = input()
    sherlock_and_anagrams(st)

'''
5
abba
abcd
cdcd
ifailuhkqq
kkkk
'''