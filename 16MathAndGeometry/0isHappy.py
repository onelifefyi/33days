# https://leetcode.com/problems/happy-number/

# Approach: Just follow the provided process
# Time O(IDK) | Space O(1)
def isHappy(n):
    def getSquaredSum(num):
        total = 0
        while num:
            total += (num % 10)**2
            num = num // 10
        return total

    numberSet = set()
    while n != 1:
        squaredSum = getSquaredSum(n)
        if squaredSum == 1:
            return True
        if squaredSum in numberSet:
            return False
        numberSet.add(squaredSum)
        n = squaredSum

n = 19
n = 2
print(isHappy(n))