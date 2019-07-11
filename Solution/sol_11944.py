# -*- coding: utf-8 -*-
# Python 3.4.5
import sys
n, m = map(int, sys.stdin.readline().split())
print((str(n)*n)[:m])