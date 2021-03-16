class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0
    
    def pushfront(self, val):
        front = ListNode(val)
        front.next = self.head
        self.head = front
        self.len += 1
    
    def popfront(self):
        if not self.head:
            return None
        val = self.head
        self.head = self.head.next
        return val
            
    def front(self):
        return self.head
        
    def __iter__(self):
        curr = self.head
        while curr != None:
            yield curr.value
            curr = curr.next

class ListNode:
    def __init__(self, val=None):
        self.value = val
        self.next = None

def generate_linked_list():
    head = None
    for i in range(10, -1, -1):
        curr = ListNode(i)
        curr.next = head
        head = curr
    return head

def reverse_linked_list(l: ListNode) -> ListNode:
    prev, following = None, None
    curr = l
    while curr:
        following = curr.next
        curr.next = prev
        prev, curr = curr, following        
    return prev

def print_linked_list(l: ListNode):
    elem = l
    while elem:
        print(elem.value, "\t", end="")
        elem = elem.next
    print()

def main():
    print("Reversing singly linked list using ListNode only")
    a = generate_linked_list()
    print("Initial: ", end="")
    print_linked_list(a)
    a = reverse_linked_list(a)
    print("Reverse: ", end="")
    print_linked_list(a)
    print("Push and pop with LinkedList class")
    b = LinkedList()
    print("pushing: ", end="")
    for i in range(10, 21):
        print(i, end="\t")
        b.pushfront(i)
    print()
    print("popping: ", end="")
    for _ in range(11):
        e = b.popfront()
        print(e.value, end="\t")
    print()
    
if __name__ == "__main__":
    main()
    

        
    
    
    

