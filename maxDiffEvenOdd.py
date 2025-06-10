class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)
        odd_counts = []
        even_counts = []
        for count in counts.values():
            if count % 2 == 1:
                odd_counts.append(count)
        for count in counts.values():
            if count % 2 == 0:
                even_counts.append(count)

        max_odd = max(odd_counts)
        max_even = min(even_counts)

        return max_odd - max_even