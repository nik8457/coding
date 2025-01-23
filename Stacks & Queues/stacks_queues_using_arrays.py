class Linear_Data_Structure:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return len(self.list) == 0

    def display(self):
        if not self.is_empty():
            for i in range(len(self.list)):
                print(i, end='----> ')
        else:
            print('List is empty')
        return None

    def push(self, data):
        self.list.append(data)
        return None

    def queue_top(self):
        if not self.is_empty():
            return self.list[-1]

    def queue_pop(self):
        if not self.is_empty():
            return self.list.pop()

    def stack_top(self):
        if not self.is_empty():
            return self.list[0]

    def stack_pop(self):
        if not self.is_empty():
            return self.list.pop(0)

a = Linear_Data_Structure()
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