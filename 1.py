
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)
    return fromPole, toPole

A = list(map(int, input().split()))
height = A[0]
fromPole=A[1]
toPole=A[2]

print(moveTower(A))
