for i in range(int(input())):
    a,b,a2,b2,a3,b3=map(list,input().split())
    if set(a+b) == set(a2+b2):
        print(1)
        continue
    if set(a+b) == set(a3+b3):
        print(2)
        continue
    else:
        print(0)