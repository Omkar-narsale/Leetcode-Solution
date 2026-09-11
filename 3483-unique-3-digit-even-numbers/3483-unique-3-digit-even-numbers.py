class Solution:
    def totalNumbers(self, digits):
        n = len(digits)
        seen = set()

        for h in range(n):
            if digits[h] == 0:
                continue

            for t in range(n):
                if t == h:
                    continue

                for u in range(n):
                    if u == h or u == t:
                        continue

                    if digits[u] % 2 != 0:
                        continue

                    num = digits[h] * 100 + digits[t] * 10 + digits[u]
                    seen.add(num)

        return len(seen)