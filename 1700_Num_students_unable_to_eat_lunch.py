from collections import deque, Counter


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        hsh = Counter(students)
        stud_q = deque(students)
        sw_q = deque(sandwiches)

        while len(stud_q) != 0:
            if hsh[0] == len(stud_q) and sw_q[0] == 1 or hsh[1] == len(stud_q) and sw_q[0] == 0:
                return len(stud_q)

            if stud_q[0] == sw_q[0]:
                a = stud_q.popleft()
                sw_q.popleft()
                hsh[a] -= 1
            else:
                a = stud_q.popleft()
                stud_q.append(a)

        return 0
