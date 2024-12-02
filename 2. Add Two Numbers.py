# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    __slots__ = ()

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        buff = 0

        def sum(node, t1=None, t2=None, buff=0):
            s1 = t1.val if t1 is not None else 0
            s2 = t2.val if t2 is not None else 0

            sum_i = s1 + s2 + buff

            if sum_i > 9:
                node.val = sum_i % 10
                buff = 1

            else:
                node.val = sum_i
                buff = 0

            if (t1 is None or t1.next is None) and (t2 is None or t2.next is None) and buff == 0:
                return

            else:
                node.next = ListNode(val=0, next=None)
                return sum(node.next, t1.next if t1 is not None else None,
                           t2.next if t2 is not None else None, buff)

        sum(ans, l1, l2)
        return ans
