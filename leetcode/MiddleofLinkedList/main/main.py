import dataclasses
from typing import Optional, TypeVar

# Definition for singly-linked list.
Node = TypeVar("Node")

@dataclasses.dataclass
class ListNode:
    val: str = 0
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
        nodes.append("None")
        return " -> ".join(nodes)

class Solution:
    def NodeSize(self, head: Optional[ListNode]) -> int:
        if head != None:
            counter = 1
        else:
            counter = 0

        while head.next != None:
            counter +=1
            head = head.next
        return counter

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = self.NodeSize(head)
        for x in size:
            node = head.next
        return node

def main():
    target = Solution()

    slist = LinkedList(ListNode(1))
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)
    node5 = ListNode(6)

    slist.head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    #print(slist)
    slist_size = target.NodeSize(slist.head)
    print(slist_size)


if __name__ == "__main__":
    main()
