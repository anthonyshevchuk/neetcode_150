# https://leetcode.com/problems/car-fleet/
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position2speed = {}
        for i, p in enumerate(position):
            position2speed[p] = speed[i]

        # sort_positions
        position.sort()

        # sort speed
        speed = [position2speed[p] for p in position]

        h_to_go = []
        fleet_count = 0

        for i in range(len(position)):
            ith_m_to_go = target - position[i]
            ith_h_to_go = ith_m_to_go / speed[i]

            # if it's the first car:
            if not h_to_go:
                fleet_count += 1
                h_to_go.append(ith_h_to_go)

            # if they can potentially meet before destination (if equal - they arrive at dest. at the same time)
            elif ith_h_to_go >= h_to_go[i - 1]:
                h_to_go.append(ith_h_to_go)

            else:
                fleet_count += 1
                h_to_go.append(ith_h_to_go)

        return fleet_count


if __name__ == '__main__':
    s = Solution()
    # print(s.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))  # 3
    # print(s.carFleet(100, [0, 2, 4], [4, 2, 1]))  # 1
    print(s.carFleet(10, [0, 4, 2], [2, 1, 3]))  # 1


