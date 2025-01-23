class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Doubly_LL:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def is_empty(self):
        return self.head.next != self.tail
    def display(self):
        if self.is_empty():
            n = self.head.next
            while n != self.tail:
                print(n.data, end= '----> ')
                n = n.next
            print()
            return
        print('Check LL once, it\'s empty ')

    def push(self, data):
        new_node = Node(data)
        last = self.tail.prev
        last.next = new_node
        new_node.prev = last
        self.tail.prev = new_node
        new_node.next = self.tail

    def queue_top(self):
        if self.is_empty():
            return self.tail.prev.data
        print('Check LL once, it\'s empty ')
        return None

    def queue_pop(self):
        if self.is_empty():
            last_node = self.tail.prev
            second_last = self.tail.prev.prev
            self.tail.prev = second_last
            second_last.next = self.tail
            return last_node.data
        print('Check LL once, it\'s empty ')
        return None

    def stack_top(self):
        if self.is_empty():
            return self.head.next.data
        print('Check LL once, it\'s empty ')
        return None

    def stack_pop(self):
        if self.is_empty():
            first_node = self.head.next
            second_node = self.head.next.next
            self.head.next = second_node
            second_node.prev = self.head
            return first_node.data
        print('Check LL once, it\'s empty ')
        return None

a = Doubly_LL()
a.display()
a.push("10")
a.push("200")
a.push("30")
a.push("40")
a.push("50")
a.display()
print(a.queue_top())
a.display()
print(a.queue_pop())
a.display()
print(a.stack_top())
a.display()
print(a.stack_pop())
a.display()
