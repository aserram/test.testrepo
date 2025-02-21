import itertools
import dataclasses
from typing import Optional, TypeVar

# Definition for singly-linked list.
Node = TypeVar("Node")

@dataclasses.dataclass
class ListNode:
    val: str = 0
    next: Node = None

class LinkedList:
    def __init__(self, head: ListNode = None) -> Optional[ListNode]:
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = ListNode()
        result_node = curr_node
        carry = 0
        while l1 or l2 or carry :
            total = carry
            if l1 is not None:
                total += l1.val
                l1 = l1.next
            if l2 is not None:
                total += l2.val
                l2 = l2.next
            sum = (total) % 10
            carry = (total) // 10
            curr_node.val = sum
            if l1 or l2 or carry:
                curr_node.next = ListNode()
                curr_node = curr_node.next
        return result_node

def main():
    target = Solution()
    node1 = ListNode(8, ListNode(8, ListNode(8)))
    node2 = ListNode(8, ListNode(8))
    sum = target.addTwoNumbers(node1, node2)
    print(sum)

if __name__ == "__main__":
    main()