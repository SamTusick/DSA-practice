class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def main():
    head = ListNode(0)

    append(head, 5)
    append(head, 6)
    append(head, 7)
    remove(head, 6)
    append(head, 6)
    append(head, 10)
    append(head, 11)
    append(head, 12)
    remove(head, 7)

    display(head)

def append(head, value):

    if head is None:
        return ListNode(value)
    
    curr = head

    while curr.next is not None:
        curr = curr.next
    curr.next = ListNode(value)

def remove(head, value):
    while head.val is not None and head.val == value:
        head = head.next

    curr = head

    while curr.next is not None:
        if curr.next.val == value:
            curr.next = curr.next.next
        curr = curr.next


def display(head):
    values = []

    if head is None:
        return values
    
    curr = head

    while curr is not None:
        values.append(curr.val)
        curr = curr.next
    
    print(values)



if __name__ == '__main__':
    main()