# https://leetcode.com/problems/meeting-rooms/
# Taken from NeetCode

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:

    # Approach:
    # First ensure that the list is sorted with start time O(nlogn)
    # Then for each meeting check if the start of next meeting is between the start and end of current meeting
    # If so, return False
    # Otherwise return True at the end
    # Time O(nlogn) | Space O(1)
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x: x.start)
        index = 0
        while index < len(intervals) - 1:
            if intervals[index].end > intervals[index + 1].start:
                return False
            index += 1
        return True