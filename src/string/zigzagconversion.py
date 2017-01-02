class solution(object):
    def convert(self, s, nrows):
        if nrows == 1:
            return s

        str_len = len(s)
        offset = 2 * nrows - 2

        res = ''

        # first row
        idx = 0
        while idx < str_len:
            res += s[idx]
            idx += offset

        # row 1~n-1
        for m in range(1, nrows - 1):
            idx = m
            while idx < str_len:
                res += s[idx]
                right_index = idx + (nrows - m - 1) * 2
                if right_index < str_len:
                    res += s[right_index]
                idx += offset

        # last row
        idx = nrows - 1
        while idx < str_len:
            res += s[idx]
            idx += offset

        return res
