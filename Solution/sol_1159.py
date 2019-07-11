# -*- coding: utf-8 -*-
# Python 3.4.5
def main() :
    n = int(input())
    cnt = [0]*26
    for i in range(n):
        cnt[ord(input()[0])-ord('a')] += 1
 
    result = []
    for i in range(26):
        if(cnt[i] >= 5):
            result.append(chr(i+ord('a')))
            
    if len(result) == 0 :
        print("PREDAJA")
    else:
        for i in range(len(result)):
            print(result[i],end="")
 
if __name__ == '__main__':
    main()