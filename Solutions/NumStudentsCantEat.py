from collections import deque
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        std = deque(students)
        sw = deque(sandwiches)

        while std and sw:
            if std[0] == sw[0] :
                std.popleft()
                sw.popleft()
            else:
                if std.count(sw[0]) == 0 :
                    break
                std.append(std.popleft())
        return len(std)

sol = Solution()
print(sol.countStudents([1, 1, 0, 0], [0, 1, 0, 1]))
print(sol.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))
