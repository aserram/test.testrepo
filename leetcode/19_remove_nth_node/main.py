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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result_ll = ListNode(0, head)
        leftp = result_ll
        rightp = head

        for _ in range(n):
            rightp = rightp.next

        while rightp:
            leftp = leftp.next
            rightp = rightp.next
        leftp.next = leftp.next.next
        return result_ll.next


def main():
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    # node1 = ListNode(1, None)
    target = Solution()
    result = LinkedList(target.removeNthFromEnd(node1, 2))
    print(result)


if __name__ == "__main__":
    main()
