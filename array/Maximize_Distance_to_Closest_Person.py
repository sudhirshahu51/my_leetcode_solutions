#problem link https://leetcode.com/problems/maximize-distance-to-closest-person/
#Maximize Distance to Closest Person

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        max_dist = 0
        last_occ = None
        max_gap = 0
        S = [i for i in range(len(seats)) if seats[i]] 
        if len(seats) != 1:
            for i in range(len(seats)):
                if seats[i] == 1:
                    seat_occ_ind = i
                    if last_occ != None:
                        if seat_occ_ind - last_occ > max_gap:
                        #max_gap = max(max_gap, seat_occ_ind - last_occ)
                            max_gap = seat_occ_ind - last_occ
                            max_dist= (max_gap)//2
                    last_occ =  seat_occ_ind
        return max(max_dist, S[0], len(seats)-1-S[-1])