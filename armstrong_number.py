import os

def armstrong(num):
    l = len(str(num))
    temp = num
    arm = 0
    while num > 0:
        n = num % 10
        arm = arm + n ** l
        num = num //10
    if temp == arm:
        print("number is armstrong")
    else:
        print("number is not armstrong")

armstrong(153)
