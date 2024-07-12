from typing import List, Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def is_critical(prev: ListNode, cur: ListNode, nxt: ListNode) -> bool:
            return (prev.val > cur.val < nxt.val) or (prev.val < cur.val > nxt.val)

        if not head or not head.next or not head.next.next:
            return [-1, -1]

        first_crit_idx, prev_crit_idx = -1, -1
        min_dist, max_dist = float('inf'), -1

        index = 1
        prev, cur, nxt = head, head.next, head.next.next

        while nxt:
            if is_critical(prev, cur, nxt):
                if first_crit_idx == -1:
                    first_crit_idx = index
                else:
                    min_dist = min(min_dist, index - prev_crit_idx)
                    max_dist = index - first_crit_idx

                prev_crit_idx = index

            prev, cur, nxt = cur, nxt, nxt.next
            index += 1

        if min_dist == float('inf'):
            min_dist = -1

        return [min_dist, max_dist]

# Example usage:
# Let's create a linked list: 1 -> 3 -> 2 -> 2 -> 3 -> 2 -> 2 -> 2
head = ListNode(1, ListNode(3, ListNode(2, ListNode(2, ListNode(3, ListNode(2, ListNode(2, ListNode(2))))))))

solution = Solution()
print(solution.nodesBetweenCriticalPoints(head))  # Output: [1, 3]
