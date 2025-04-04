import dataclasses
from typing import Optional, TypeVar


# Definition for singly-linked list.
Node = TypeVar("Node")


@dataclasses.dataclass
class ListNode:
    val: int = 0
    next: Node = None


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        pointer = dummy
        while list1 or list2:
            if list1.val <= list2.val:
                dummy.val = list1.val
                dummy.next = ListNode(list2.val, ListNode())
            else:
                dummy.val = list2.val
                dummy.next = ListNode(list1.val, ListNode())

            list1 = list1.next
            list2 = list2.next
            dummy = dummy.next.next
        return pointer


def main():
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    target = Solution()
    target.mergeTwoLists(list1, list2)


if __name__ == "__main__":
    main()
