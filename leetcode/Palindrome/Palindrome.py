from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ln_to_list = []
        while head is not None:
            ln_to_list.append(head.val)
            head = head.next

        while len(ln_to_list) > 1:
            first = ln_to_list.pop(0)
            last = ln_to_list.pop()
            if first != last:
                return False
        return True


def main():
    slist = LinkedList(ListNode(1))

    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(2)
    node4 = ListNode(1)

    slist.head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    print(slist)
    solution = Solution()
    result = solution.isPalindrome(slist.head)
    if result:
        print(f"The linked list is a palindrome")
    else:
        print(f"The linked list is not a palindrome")


if __name__ == "__main__":
    main()
