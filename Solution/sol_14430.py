# -*- coding: utf-8 -*-
# Python 3.4.5
import sys
def go(x, y, dp, data) :
    if x < 0 or y < 0 :
        return 0 # 올바르지 않은 값
    if dp[x][y] != -1 :
        return dp[x][y] # 이미 연산된 값
    # 처음 연산하는 경우
    dp[x][y] = data[x][y]
    dp[x][y] += max(go(x-1, y, dp, data), go(x, y-1, dp, data))
    return dp[x][y]
 
# Main
if __name__ == '__main__':
    # 입력
    n, m = map(int, sys.stdin.readline().split())
    data = []
    for i in range(n) :
        temp = list(map(int, sys.stdin.readline().split()))
        data.append(temp)
    # 다이나믹
    dp =[[-1] * m for _ in range(n)]
    dp[0][0] = data[0][0]
    # 결과
    print(go(n-1,m-1, dp, data))