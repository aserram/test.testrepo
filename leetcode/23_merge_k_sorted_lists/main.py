import dataclasses
from typing import List, Optional, TypeVar


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
        dummy = ListNode(0)
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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for idx in range(0, len(lists), 2):
                list1 = lists[idx]
                list2 = lists[idx + 1] if idx + 1 < len(lists) else None
                merged.append(self.mergeTwoLists(list1, list2))
            lists = merged
        return lists.pop()


def main():
    target = Solution()
    linked_one = ListNode(1, ListNode(4, ListNode(5)))
    linked_two = ListNode(1, ListNode(3, ListNode(4)))
    linked_three = ListNode(2, ListNode(6))
    result = target.mergeKLists([linked_one, linked_two, linked_three])
    print(LinkedList(result))


if __name__ == "__main__":
    main()
