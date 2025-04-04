import dataclasses
from typing import Optional, TypeVar


# Definition for singly-linked list.
Node = TypeVar("Node")


@dataclasses.dataclass
class ListNode:
    val: int = 0
    next: Node = None


class LinkedList:
    def __init__(self, head: ListNode = None):
        self.head = head

    def __str__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.val))
            node = node.next
        return f"[{",".join(nodes)}]"


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        pointer = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next

        if list1:
            dummy.next = list1
        else:
            dummy.next = list2

        return pointer.next


def main():
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    target = Solution()
    print(LinkedList(target.mergeTwoLists(list1, list2)))


if __name__ == "__main__":
    main()
