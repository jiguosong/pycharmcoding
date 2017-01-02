
class solution(object):
    def twosum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = dict()
        size = len(nums)
        for i in range(size):
            map[nums[i]] = i
        for i in range(size):
            inx1 = i
            inx2 = map.get(target - nums[inx1])
            if inx2 and inx2 != inx1:
                return inx1 + 1, inx2 + 1

        return -1, -1
