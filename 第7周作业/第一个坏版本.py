N = int(input())
isBadVersion = eval(input())
 
def firstBadVersion(n):
    left = 1
    right = n
    while left < right:
        midpoint = (left + right)//2
        if isBadVersion(midpoint):
            right = midpoint
        else:
            left = midpoint + 1
    return left
 
print(firstBadVersion(N))