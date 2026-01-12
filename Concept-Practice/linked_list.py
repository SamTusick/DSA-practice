class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def main():
    n1 = ListNode(4)
    n2 = ListNode(7)
    n3 = ListNode(9)
    n1.next = n2
    n2.next = n3


    current = n1

    while current is not None:
        print(current.val)
        current = current.next

if __name__ == '__main__':
    main()