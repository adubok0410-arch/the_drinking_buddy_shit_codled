class Solution:
    def romanToInt(self, s: str) -> int:
        def val(ch: str) -> int:
            if ch == 'I':
                return 1
            if ch == 'V':
                return 5
            if ch == 'X':
                return 10
            if ch == 'L':
                return 50
            if ch == 'C':
                return 100
            if ch == 'D':
                return 500
            return 1000  

        total = 0
        prev = 0

        for i in range(len(s) - 1, -1, -1):
            cur = val(s[i])
            if cur < prev:
                total -= cur
            else:
                total += cur
            prev = cur

        return total