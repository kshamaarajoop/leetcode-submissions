from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for i in range(len(nums)):
            #remove the elements outside the window
            while q and q[0]<= i-k:
                q.popleft()
            
            #remove the smaller values in the the queue
            while q and nums[i]>= nums[q[-1]]:
                q.pop()
            q.append(i)

            #when the queue is ready
            if i>=k- 1:
                ans.append(nums[q[0]])


        return ans
