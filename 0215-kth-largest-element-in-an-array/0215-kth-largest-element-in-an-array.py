import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        l=[]
        for n in nums:
            heapq.heappush(l,n)

            if len(l)>k:
                heapq.heappop(l)
        return l[0]

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna