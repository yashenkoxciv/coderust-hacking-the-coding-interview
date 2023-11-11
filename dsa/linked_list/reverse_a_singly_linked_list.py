from linkedlist import LinkedList, LinkedListNode


def reverse(head: LinkedListNode):
    if (head is None) or (head.next is None):
        return head

    reversed = head
    old_head = head.next
    reversed.next = None

    while old_head.next:
        temp = old_head
        old_head = old_head.next
        temp.next = reversed
        reversed = temp
    temp = old_head
    temp.next = reversed
    reversed = temp
    
    return reversed

# TODO: tests