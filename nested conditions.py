ac_date=list(map(int, input().split()))
ex_date=list(map(int, input().split()))
#x=int(n.split())
print(n)
print(x)
assert (1<=n[0]<=31 and 1<=n[1]<=12 and 1<=n[2]<=3000)
assert (1<=x[0]<=31 and 1<=x[1]<=12 and 1<=x[2]<=3000)
#print(x[0]>x[2])
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=list(map(int, input().split()))  #actual date
x=list(map(int, input().split())) #expected date
assert (1<=n[0]<=31 and 1<=n[1]<=12 and 1<=n[2]<=3000)
assert (1<=x[0]<=31 and 1<=x[1]<=12 and 1<=x[2]<=3000)

if n[2]>x[2]:
    fine=10000
elif n[1]==x[1]:
    if n[1]>x[1]:
        fine=500*(n[1]-x[1])
    elif n[1]==x[1]:
        if n[0]>x[0]:
            fine=15*(n[0]-x[0])
        elif n[0]<=x[0]:
            fine=0
    else:
        fine=0
else:
    fine=0

print(fine)
"""
