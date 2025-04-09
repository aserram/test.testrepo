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
        dummy1 = ListNode(0, head)
        result = dummy1
        dummy2 = dummy1.next

        while dummy2 and dummy2.next:
            dummy1.next = dummy2.next
            dummy1 = dummy1.next
            dummy2.next = dummy1.next
            dummy1.next = dummy2

            dummy1 = dummy1.next
            dummy2 = dummy2.next
        return result.next


def main():
    nodes = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    target = Solution()
    result = target.swapPairs(nodes)
    print(LinkedList(result))


if __name__ == "__main__":
    main()
