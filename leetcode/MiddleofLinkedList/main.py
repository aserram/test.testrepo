import dataclasses
from typing import Optional


@dataclasses.dataclass
class ListNode:
    val: int = 0
    next: Optional["ListNode"] = None


# pylint: disable=too-few-public-methods
class LinkedList:
    def __init__(self, head: Optional[ListNode] = None):
        self.head = head

    def __str__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.val))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


class Solution:
    def NodeSize(self, head: Optional[ListNode]) -> int:
        counter = 0
        while head is not None:
            counter += 1
            head = head.next

        return counter

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        current: ListNode = head
        size = self.NodeSize(current)

        if size % 2 == 0:
            middle = int((size / 2) + 1)
        else:
            middle = int((size + 1) / 2)

        for _ in range(middle - 1):
            assert current.next is not None
            current = current.next
        return current


def main():
    target = Solution()

    slist = LinkedList(ListNode(1))
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)
    # node5 = ListNode(6)

    assert slist.head is not None
    slist.head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    middle_node = target.middleNode(slist.head)
    middle_slist = LinkedList(middle_node)
    print(middle_slist)


if __name__ == "__main__":
    main()
