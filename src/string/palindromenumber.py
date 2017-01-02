import math


class solution(object):
    def isPalindromenumber(self, num):
        k = 0
        p = num

        while p != 0:
            k = k * 10 + p % 10;
            p = math.floor(p / 10);

        return k == num
