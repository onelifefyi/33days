# https://leetcode.com/problems/last-stone-weight/

# Approach:
# This is a case where we want to maintain a sorted data structure
# As each time we destroy, it gets a new weight
# We can use heap to maintain the list

import heapq
def lastStoneWeight(stones):
    # Doing this to create max heap instead of min heap
    stones = [-1 * stone for stone in stones]
    # This will take O(n) time
    heapq.heapify(stones)

    while len(stones) > 1:
        s1 = heapq.heappop(stones)
        s2 = heapq.heappop(stones)
        if s1 == s2: continue
        heapq.heappush(stones, s1 - s2)
    return -stones[0] if stones else 0



# stones = [2,7,4,1,8,1]
# stones = [1]
stones = [2, 2]
print(lastStoneWeight(stones))