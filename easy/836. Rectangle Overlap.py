class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        #top left -> x1,y2
        #bottom left -> x1,y1
        #top right -> x2,y2
        #bottom right -> x2,y1
        #interval overlap
        if rec1[2]>rec2[0] and rec1[0]<rec2[2] and rec1[3]>rec2[1] and rec1[1]<rec2[3]:
            return True
        else:
            return False
