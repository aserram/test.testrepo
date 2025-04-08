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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass


def main():
    target = Solution()
    linked_one = ListNode(1, ListNode(4, ListNode(5)))
    linked_two = ListNode(1, ListNode(3, ListNode(4)))
    linked_three = ListNode(2, ListNode(6))
    result = target.mergeKLists([linked_one, linked_two, linked_three])
    print(LinkedList(result))


if __name__ == "__main__":
    main()
