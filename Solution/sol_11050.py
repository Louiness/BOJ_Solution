# -*- coding: utf-8 -*-
# Python 3.4.5
import sys
memo = [0] * 11
def factorial(num) :
    if num <= 1:
        memo[num] = 1
        return memo[num]
    # 이미 계산된 값
    if memo[num] != 0:
        return memo[num]
    # memoization
    memo[num] = num * factorial(num-1)
    return memo[num]
# Main
if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    print(factorial(n)//(factorial(k)*factorial(n-k)))