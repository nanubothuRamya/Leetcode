class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        x0,y0=coordinates[0]
        x1,y1=coordinates[1]
        dx=x1-x0
        dy=y1-y0
        for i in range(2,len(coordinates)):
            xi,yi=coordinates[i]
            if dx*(yi-y0)!=dy*(xi-x0):
                return False
        return True
