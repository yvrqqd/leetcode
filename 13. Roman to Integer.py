class Solution:
    def romanToInt(self, s: str) -> int:
        x = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        prev_val = 0
        total_sum = 0

        for i in range(len(s)):
            if x[s[i]] > prev_val:
                total_sum -= 2 * prev_val

            prev_val = x[s[i]]
            total_sum += x[s[i]]

        return total_sum
