# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        i=0
        j=n
        cur = -1
        while(i<=j):
            mid=(i+j) // 2
            print(mid)
            if isBadVersion(mid):
                cur = mid
                j = mid-1
            else:
                i=mid+1
                
        return cur
        
