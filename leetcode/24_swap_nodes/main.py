from dataclasses import dataclass
from typing import Optional, TypeVar

Node = TypeVar("Node")


@dataclass
class ListNode:
    val: str = 0
    next: Node = None


class LinkedList:
    def __init__(self, head: Node):
        self.head = head

    def __str__(self):
        nodes = []
        while self.head:
            nodes.append(str(self.head.val))
            self.head = self.head.next
        return ",".join(nodes)


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        result = dummy

        dummy.next = head
        l1 = head
        l2 = head.next
        dummy.next = l2
        l1.next = l2.next
        l2.next = l1

        l2 = l1.next
        l1.next = l2.next
        l1 = l1.next
        l2.next = l1.next
        l1.next = l2

        pass


def main():
    nodes = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    target = Solution()
    result = target.swapPairs(nodes)
    print(LinkedList(result))


if __name__ == "__main__":
    main()
