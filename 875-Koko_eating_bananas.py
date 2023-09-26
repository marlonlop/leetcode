class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minK = r

        while l <= r:
            eatSpeed = l + ((r - l) // 2)
            hrSpent = 0
            for pile in piles:
                hrSpent += math.ceil(pile / eatSpeed)
            if hrSpent <= h:
                r = eatSpeed - 1
                minK = min(eatSpeed, minK)
            else: # hrSpent > h
                l = eatSpeed + 1
            
        return minK

'''
Find bug in code below
fails with test case:
piles =[332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184]
h=823855818

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        pLen = len(piles) - 1
        minK = None
        if len(piles) == 1:
            return math.ceil(piles[0] / h)

        while l <= r:
            eatSpeed = l + ((r - l) // 2)
            hrSpent = 0
            #print(eatSpeed)
            for i, pile in enumerate(piles):
                hrSpent += math.ceil(pile / eatSpeed)
                if hrSpent == h and i == pLen:
                    minK = min(eatSpeed, minK) if minK else eatSpeed
                    l = eatSpeed + 1
                    print(eatSpeed)
                elif hrSpent < h and i == pLen:
                    r = eatSpeed - 1
                    #minK = min(eatSpeed, minK) if minK else eatSpeed
                elif hrSpent > h and i == pLen:
                    l = eatSpeed + 1
                    #minK = min(eatSpeed, minK) if minK else eatSpeed
            
        return minK if minK else 0 #added condition to see which test case was failing
'''